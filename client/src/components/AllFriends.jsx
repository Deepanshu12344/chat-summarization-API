import React, { useState } from 'react';
import { IoSearch } from "react-icons/io5";
import { TbMessageCircleFilled } from "react-icons/tb";
import { useNavigate } from 'react-router-dom';

export const AllFriends = () => {
  const navigate = useNavigate();
  const [chatId, setChatId] = useState('10211112091')
  const users = [
    { name: "shalu12", image_url: "/image/1", status: "online" },
    { name: "harsh_0912", image_url: "/image/2", status: "online" },
    { name: "hemi_hemant", image_url: "/image/3", status: "offline" }
  ];

  return (
    <div className="p-4 text-white space-y-4">
      {/* Search bar */}
      <div className="relative w-full">
        <input
          type="text"
          placeholder="Search"
          className="w-full h-10 pl-4 pr-10 rounded-md bg-[#121214] text-white focus:outline-none border border-[#29292d] focus:border-[#5865f2]"
        />
        <IoSearch className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400" />
      </div>

      {/* User cards */}
      <div className="space-y-4">
        {users.map((user, index) => (
          <div
            onClick={()=>{navigate(`/${chatId}`)}}
            key={index}
            className="flex items-center justify-between bg-[#1e1f22] p-3 rounded-lg cursor-pointer"
          >
            {/* Left: Avatar and user info */}
            <div className="flex items-center gap-3">
              <img
                src={user.image_url}
                alt={user.name}
                className="w-10 h-10 rounded-full bg-gray-600"
              />
              <div className="flex flex-col">
                <span className="font-medium">{user.name}</span>
                <span
                  className={`text-sm ${
                    user.status === 'online' ? 'text-green-400' : 'text-gray-400'
                  }`}
                >
                  {user.status}
                </span>
              </div>
            </div>

            {/* Right: Message and Remove buttons */}
            <div className="flex items-center gap-3">
              <button>
                <TbMessageCircleFilled
                  size={22}
                  className="text-gray-400 hover:text-white transition"
                  title="Message"
                />
              </button>
              <button className="h-9 px-4 text-sm border border-[#c06463] text-white font-medium rounded-md hover:bg-[#c06463] transition">
                Remove Friend
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
