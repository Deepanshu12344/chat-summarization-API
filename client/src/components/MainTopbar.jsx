import React from 'react';
import { ImPacman } from "react-icons/im";

export const MainTopbar = ({ activeTab, setActiveTab }) => {
  return (
    <div className="bg-[#1a1a1e] h-12 w-full px-4 flex items-center gap-7">
      {/* Left section with icon and title */}
      <div className="flex items-center gap-2 text-white font-semibold text-sm">
        <ImPacman className="text-lg" />
        Friends
      </div>

      {/* Buttons right next to title */}
      <div className="flex gap-3">
        <button
          onClick={() => setActiveTab('all')}
          className={`text-sm h-8 px-4 rounded-md ${
            activeTab === 'all' ? 'bg-[#2c2c30] text-white' : 'text-white'
          }`}
        >
          All
        </button>
        <button
          onClick={() => setActiveTab('add')}
          className={`text-sm h-8 px-4 rounded-md ${
            activeTab === 'add' ? 'bg-[#5865f2] text-white' : 'bg-[#5865f2] text-white'
          }`}
        >
          Add Friend
        </button>
      </div>
    </div>
  );
};
