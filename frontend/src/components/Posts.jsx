import React from 'react';

const Posts = ({ posts }) => {
  return (
    <div className="mb-6">
      <h3 className="text-xl font-semibold mb-4">Recent Posts</h3>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {posts.map(post => (
          <div key={post.post_id} className="bg-white shadow-lg rounded-lg overflow-hidden">
            <img src={post.image_url} alt="Post" className="w-full h-48 object-cover" />
            <div className="p-4">
              <p className="text-gray-600">{post.caption.slice(0, 100)}...</p>
              <p className="text-sm mt-2">Likes: {post.likes} | Comments: {post.comments}</p>
              <p className="text-sm">Tags: {post.tags.join(', ')}</p>
              <p className="text-sm">Vibe: {post.vibe} | Quality: {post.quality}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Posts;