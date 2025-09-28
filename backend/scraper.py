import instaloader
import os
import time
from database import save_profile, save_posts, save_reels
from analysis import analyze_image, analyze_video

L = instaloader.Instaloader()

def scrape_influencer(username='therock'):
    try:
        # Load credentials from environment variables
        ig_username = os.getenv("IG_USERNAME")
        ig_password = os.getenv("IG_PASSWORD")
        
        # Attempt login if credentials provided
        if ig_username and ig_password:
            try:
                session_file = f"session-{ig_username}"
                L.load_session_from_file(ig_username, session_file)
                print(f"Loaded session for {ig_username}")
            except FileNotFoundError:
                L.login(ig_username, ig_password)
                L.save_session_to_file(session_file)
                print(f"Logged in and saved session for {ig_username}")
        else:
            print("No login credentials provided, attempting anonymous scraping")

        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)

        # Fetch profile
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Basic info
        profile_data = {
            'name': profile.full_name,
            'username': profile.username,
            'profile_pic_url': profile.profile_pic_url,
            'followers': profile.followers,
            'following': profile.followees,
            'posts_count': profile.mediacount,
            'avg_likes': 0,
            'avg_comments': 0,
            'engagement_rate': 0
        }
        
        # Fetch posts and reels
        posts = []
        reels = []
        total_likes = 0
        total_comments = 0
        post_count_for_avg = 0
        
        for post in profile.get_posts():
            if len(posts) >= 10 and len(reels) >= 5:
                break
            
            # Add delay to avoid rate limits
            time.sleep(8)
            
            if post.is_video and len(reels) < 5:
                thumbnail_path = f"data/{post.shortcode}_thumbnail.jpg"
                L.download_pic(thumbnail_path, post.display_url, post.date_utc)
                analysis = analyze_video(thumbnail_path)
                reels.append({
                    'reel_id': post.shortcode,
                    'thumbnail_url': post.display_url,
                    'caption': post.caption or '',
                    'views': post.video_view_count or 0,
                    'likes': post.likes,
                    'comments': post.comments,
                    'tags': analysis['tags'],
                    'vibe': analysis['vibe'],
                    'events': analysis['events']
                })
            elif not post.is_video and len(posts) < 10:
                image_path = f"data/{post.shortcode}.jpg"
                L.download_pic(image_path, post.display_url, post.date_utc)
                analysis = analyze_image(image_path)
                posts.append({
                    'post_id': post.shortcode,
                    'image_url': post.display_url,
                    'caption': post.caption or '',
                    'likes': post.likes,
                    'comments': post.comments,
                    'tags': analysis['tags'],
                    'vibe': analysis['vibe'],
                    'quality': analysis['quality']
                })
            
            total_likes += post.likes
            total_comments += post.comments
            post_count_for_avg += 1
        
        if post_count_for_avg > 0:
            profile_data['avg_likes'] = total_likes / post_count_for_avg
            profile_data['avg_comments'] = total_comments / post_count_for_avg
            profile_data['engagement_rate'] = (
                ((total_likes + total_comments) / post_count_for_avg)
                / profile_data['followers'] * 100
            )
        
        # Save to database
        save_profile(profile_data)
        save_posts(posts)
        save_reels(reels)
        
        return profile_data, posts, reels

    except Exception as e:
        print(f"Scraping error: {str(e)}")
        # Fallback to mock data
        profile_data = {
            'name': 'Demon Slayer',
            'username': 'tanjiro',
            'profile_pic_url': '/images/pic_one.jpg',
            'followers': 400000000,
            'following': 200,
            'posts_count': 7000,
            'avg_likes': 1000000,
            'avg_comments': 5000,
            'engagement_rate': 0.25
        }
        posts = [
            {
                'post_id': f'post_{i}',
                'image_url': f'/images/posts/post{i}.jpg',
                'caption': f'Sample post {i} by The Rock',
                'likes': 100000 + i * 1000,
                'comments': 2000 + i * 100,
                'tags': ['fitness', 'motivation'],
                'vibe': 'energetic',
                'quality': 'high'
            } for i in range(1, 11)
        ]
        reels = [
            {
                'reel_id': f'reel_{i}',
                'thumbnail_url': f'/images/reels/reel{i}.jpg',
                'caption': f'Sample reel {i} by The Rock',
                'views': 2000000 + i * 10000,
                'likes': 150000 + i * 1000,
                'comments': 3000 + i * 100,
                'tags': ['motivation', 'workout'],
                'vibe': 'energetic',
                'events': ['training', 'speech']
            } for i in range(1, 6)
        ]
        save_profile(profile_data)
        save_posts(posts)
        save_reels(reels)
        return profile_data, posts, reels
