import React from 'react';

const Profile = ({ profile }) => {
  return (
    <div className="bg-white shadow-lg rounded-lg overflow-hidden mb-6">
      <img src={profile.profile_pic_url} alt="Profile" className="w-full h-48 object-cover" />
      <div className="p-4">
        <h2 className="text-2xl font-bold">{profile.name} (@{profile.username})</h2>
        <p className="text-gray-600 mt-2">
          Followers: {profile.followers}<br />
          Following: {profile.following}<br />
          Posts: {profile.posts_count}
        </p>
      </div>
    </div>
  );
};

export default Profile;