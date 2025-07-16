import React from 'react';
import { IoSearch } from "react-icons/io5";

export const AllFriends = () => {
  const users = [
    { name: "shalu12", image_url: "/image/1", status: "online" },
    { name: "harsh_0912", image_url: "/image/2", status: "online" },
    { name: "hemi_hemant", image_url: "/image/3", status: "offline" }
  ];

  return (
    <div className="p-4 text-white space-y-4">
      <div className="relative w-full">
  {/* Search Input with Icon */}
  <input
    type="text"
    placeholder="Search"
    className="w-full h-10 pl-4 pr-10 rounded-md bg-[#121214] text-white focus:outline-none border border-[#29292d] focus:border-[#5865f2]" 
  />
  <IoSearch className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400" />
</div>

      {/* Users List */}
      <div className="space-y-4">
        {users.map((user, index) => (
          <div key={index} className="flex items-center gap-3 bg-[#1e1f22] p-3 rounded-lg">
            <img
              src={user.image_url}
              alt={user.name}
              className="w-10 h-10 rounded-full bg-gray-600"
            />
            <div className="flex flex-col">
              <span className="font-medium">{user.name}</span>
              <span className={`text-sm ${user.status === 'online' ? 'text-green-400' : 'text-gray-400'}`}>
                {user.status}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );    
};
