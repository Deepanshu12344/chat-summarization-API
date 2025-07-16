import React from 'react';
import { FaArrowLeftLong } from "react-icons/fa6";
import './gradient.css'; // Import the custom animation

export const MainRightbar = () => {
  return (
    <div className="h-screen w-52 bg-[#202024] text-white px-4 py-6">
      <p className="font-semibold text-sm mb-3">Active Now</p>

      {/* Animated gradient border */}
      <div className="animated-gradient p-[2px] rounded-md mb-4">
        <input
          type="text"
          placeholder="Say Something"
          className="w-full h-9 px-3 text-sm rounded-md bg-[#202024] text-white focus:outline-none"
        />
      </div>

      <FaArrowLeftLong className="text-xl hover:text-gray-300 cursor-pointer transition" />
    </div>
  );
};
