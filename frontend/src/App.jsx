import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Profile from './components/Profile';
import Analytics from './components/Analytics';
import Posts from './components/Posts';
import Reels from './components/Reels';

const App = () => {
  const [profile, setProfile] = useState(null);
  const [posts, setPosts] = useState([]);
  const [reels, setReels] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/scrape')
      .then(() => {
        axios.get('http://127.0.0.1:8000/profile').then(res => setProfile(res.data));
        axios.get('http://127.0.0.1:8000/posts').then(res => setPosts(res.data));
        axios.get('http://127.0.0.1:8000/reels').then(res => setReels(res.data));
      })
      .catch(err => console.error(err));
  }, []);

  if (!profile) return <div className="text-center text-gray-500 mt-10">Loading...</div>;

  return (
    <div className="container mx-auto p-4 max-w-7xl">
      <Profile profile={profile} />
      <Analytics profile={profile} posts={posts} />
      <Posts posts={posts} />
      <Reels reels={reels} />
    </div>
  );
};

export default App;