import React, { useState } from 'react';
import { MainSidebar } from './MainSidebar';
import { MainTopbar } from './MainTopbar';
import { AllFriends } from './AllFriends';
import { AddFriend } from './AddFriend';
import { MainRightbar } from './MainRightbar';

export const Main = () => {
  const [activeTab, setActiveTab] = useState('all');

  return (
    <div className="fixed flex bg-[#1a1a1e] top-8 left-20 w-screen h-screen border border-[#29292d] rounded-xl">
      {/* Optional: top hr line */}
      <hr className="absolute top-12 left-0 w-full border-[#29292d]" />

      {/* Sidebar */}
      <div className="max-w-[400px]">
        <MainSidebar />
      </div>

      {/* Right content: Topbar + Friends/AddFriend */}
      <div className="flex-1 flex flex-col">
        {/* Topbar */}
        <MainTopbar activeTab={activeTab} setActiveTab={setActiveTab} />

        {/* Content below Topbar */}
        <div className="flex-1 overflow-y-auto px-4 py-6">
          {activeTab === 'all' ? <AllFriends /> : <AddFriend />}
        </div>
      </div>

     <div className="w-60 border-l border-[#29292d]">
  <MainRightbar />
</div>
    </div>
  );
};
