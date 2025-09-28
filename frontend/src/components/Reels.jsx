import React from 'react';

const Reels = ({ reels }) => {
  return (
    <div>
      <h3 className="text-xl font-semibold mb-4">Recent Reels</h3>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {reels.map(reel => (
          <div key={reel.reel_id} className="bg-white shadow-lg rounded-lg overflow-hidden">
            <img src={reel.thumbnail_url} alt="Reel" className="w-full h-48 object-cover" />
            <div className="p-4">
              <p className="text-gray-600">{reel.caption.slice(0, 100)}...</p>
              <p className="text-sm mt-2">Views: {reel.views} | Likes: {reel.likes} | Comments: {reel.comments}</p>
              <p className="text-sm">Tags: {reel.tags.join(', ')}</p>
              <p className="text-sm">Vibe: {reel.vibe}</p>
              <p className="text-sm">Events: {reel.events.join(', ')}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Reels;