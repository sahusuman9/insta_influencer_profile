import sqlite3

DB_NAME = "influencer.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Profile table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY,
        name TEXT,
        username TEXT,
        profile_pic_url TEXT,
        followers INTEGER,
        following INTEGER,
        posts_count INTEGER,
        avg_likes REAL,
        avg_comments REAL,
        engagement_rate REAL
    )
    ''')
    
    # Posts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id TEXT,
        image_url TEXT,
        caption TEXT,
        likes INTEGER,
        comments INTEGER,
        tags TEXT,  -- Comma-separated tags
        vibe TEXT,
        quality TEXT
    )
    ''')
    
    # Reels table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reel_id TEXT,
        thumbnail_url TEXT,
        caption TEXT,
        views INTEGER,
        likes INTEGER,
        comments INTEGER,
        tags TEXT,
        vibe TEXT,
        events TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def save_profile(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO profile (id, name, username, profile_pic_url, followers, following, posts_count, avg_likes, avg_comments, engagement_rate)
    VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data['name'], data['username'], data['profile_pic_url'], data['followers'], data['following'], data['posts_count'],
          data['avg_likes'], data['avg_comments'], data['engagement_rate']))
    conn.commit()
    conn.close()

def save_posts(posts):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    for post in posts:
        cursor.execute('''
        INSERT INTO posts (post_id, image_url, caption, likes, comments, tags, vibe, quality)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (post['post_id'], post['image_url'], post['caption'], post['likes'], post['comments'],
              ','.join(post['tags']), post['vibe'], post['quality']))
    conn.commit()
    conn.close()

def save_reels(reels):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    for reel in reels:
        cursor.execute('''
        INSERT INTO reels (reel_id, thumbnail_url, caption, views, likes, comments, tags, vibe, events)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (reel['reel_id'], reel['thumbnail_url'], reel['caption'], reel['views'], reel['likes'], reel['comments'],
              ','.join(reel['tags']), reel['vibe'], ','.join(reel['events'])))
    conn.commit()
    conn.close()

def get_profile():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profile WHERE id=1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'name': row[1], 'username': row[2], 'profile_pic_url': row[3],
            'followers': row[4], 'following': row[5], 'posts_count': row[6],
            'avg_likes': row[7], 'avg_comments': row[8], 'engagement_rate': row[9]
        }
    return None

def get_posts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return [{
        'post_id': row[1], 'image_url': row[2], 'caption': row[3],
        'likes': row[4], 'comments': row[5], 'tags': row[6].split(','),
        'vibe': row[7], 'quality': row[8]
    } for row in rows]

def get_reels():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reels LIMIT 5")
    rows = cursor.fetchall()
    conn.close()
    return [{
        'reel_id': row[1], 'thumbnail_url': row[2], 'caption': row[3],
        'views': row[4], 'likes': row[5], 'comments': row[6],
        'tags': row[7].split(','), 'vibe': row[8], 'events': row[9].split(',')
    } for row in rows]