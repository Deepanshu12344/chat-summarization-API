import React, { useRef, useEffect, useState } from 'react';

export const MainSidebar = () => {
  const [tab, setTab] = useState('friends')
  const sidebarRef = useRef(null);
  const isResizingRef = useRef(false);

  useEffect(() => {
    const handleMouseMove = (e) => {
      if (!isResizingRef.current || !sidebarRef.current) return;

      const newWidth = e.clientX;
      if (newWidth >= 150 && newWidth <= 600) {
        sidebarRef.current.style.width = `${newWidth}px`;
      }
    };

    const handleMouseUp = () => {
      isResizingRef.current = false;
    };

    // Attach on mount
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);

    // Cleanup on unmount
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);

  const startResizing = (e) => {
    e.preventDefault();
    isResizingRef.current = true;
  };

  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <div
        ref={sidebarRef}
        className="bg-[#121214] rounded-tl-xl h-full text-white"
        style={{ width: '300px', minWidth: '260px', maxWidth: '450px'  }}
      >
        <div className='h-12 p-2'>
            <button className='text-[13px] h-full w-full rounded-lg bg-[#222225]'>Find or start a conversation</button>
        </div>

        <div className='flex flex-col gap-3 w-full h-28 p-2'>
            <button onClick={()=>{setTab('friends')}} className='text-sm h-10 w-full rounded-lg bg-[#2c2c30]'>Friends</button>
            <button onClick={()=>{setTab('Request')}} className='text-sm h-10 w-full rounded-lg bg-[#2c2c30]'>Request</button>
        </div>
      </div>

      {/* Drag handle */}
      <div
        onMouseDown={startResizing}
        className="w-[3px] cursor-ew-resize  bg-[#121214]"
        style={{ height: '100%' }}
      ></div>
    </div>
  );
};


