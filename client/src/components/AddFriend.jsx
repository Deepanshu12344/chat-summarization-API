import React from 'react';

export const AddFriend = () => {
  
  const handleSubmit = () =>{
    console.log("Got it!");
  }

  const msg = "You can add friends with their Username";

  return (  
    <div className="text-white px-4 py-6 space-y-4 flex flex-col items-start text-left">
      {/* Header Section */}
      <div>
        <p className="text-xl font-semibold">Add Friend</p>
        <p className="text-sm text-gray-400">{msg}</p>
      </div>

      {/* Input with Button Inside */}
      <div className="relative w-full">
            <input
                className="bg-[#1e1f22] text-white w-full h-14 pl-4 pr-44 rounded-lg focus:outline-none border border-[#1e1f22] focus:border-[#5865f2] placeholder:text-gray-400"
                type="text"
                name="username"
                placeholder={msg}
            />
            <button
                onClick={handleSubmit}
                className="absolute right-2 top-1/2 -translate-y-1/2 h-9 px-4 bg-[#5865f2] text-sm font-medium rounded-md hover:bg-[#4752c4] transition"
            >
            Send Request
            </button>
      </div>
    </div>
  );
};
