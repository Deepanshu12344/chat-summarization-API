import React from 'react';
import { RiSettings4Fill } from "react-icons/ri";

export const Profile = () => {
  const user = [
    { name: "Deepanshu1209", status: "online" }
  ];

  return (
    <div className="bg-[#202024] w-80 h-20 rounded-lg p-4 flex items-center justify-between text-white shadow-md">
      {/* Left: Avatar + Info */}
      <div className="flex items-center gap-4">
        {/* Avatar placeholder (you can replace src later) */}
        <div className="w-10 h-10 rounded-full bg-gray-600 flex items-center justify-center text-sm">
          {/* fallback initials */}
          {user[0].name[0].toUpperCase()}
        </div>

        {/* Username and status */}
        <div className="flex flex-col leading-tight">
          <span className="font-medium">{user[0].name}</span>
          <span className="text-xs text-green-400">{user[0].status}</span>
        </div>
      </div>

      {/* Right: Settings icon */}
      <button className="hover:bg-[#2c2c30] p-2 rounded-md transition">
        <RiSettings4Fill size={20} />
      </button>
    </div>
  );
};
