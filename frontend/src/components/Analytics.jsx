import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const Analytics = ({ profile, posts }) => {
  const data = {
    labels: posts.map(p => p.post_id.slice(0, 5)),
    datasets: [
      { label: 'Likes', data: posts.map(p => p.likes), backgroundColor: 'rgba(75,192,192,0.6)' },
      { label: 'Comments', data: posts.map(p => p.comments), backgroundColor: 'rgba(153,102,255,0.6)' }
    ]
  };

  return (
    <div className="bg-white shadow-lg rounded-lg p-6 mb-6">
      <h3 className="text-xl font-semibold mb-4">Analytics</h3>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
        <p>Avg Likes: {profile.avg_likes.toFixed(2)}</p>
        <p>Avg Comments: {profile.avg_comments.toFixed(2)}</p>
        <p>Engagement Rate: {profile.engagement_rate.toFixed(2)}%</p>
      </div>
      <div className="w-full">
        <Bar data={data} options={{ responsive: true }} />
      </div>
    </div>
  );
};

export default Analytics;