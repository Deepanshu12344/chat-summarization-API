import React,{useState} from 'react'
import { ImPacman } from "react-icons/im";
import { MdInbox } from "react-icons/md";
import { IoMdHelp } from "react-icons/io";

export const Topbar = () => {
  const [tag, setTag] = useState("Friends");
  return (
    <div className='flex justify-end bg-[#121214] h-8'>
        <div className='flex justify-between w-1/2 px-2'>
            <div className='flex grid-flow-row grid-cols-2 justify-center items-center gap-2 w-24'>
                <ImPacman />
                <span>{tag}</span>
            </div>
            <div className='flex justify-center items-center gap-2 w-24'>
                <MdInbox />
                <IoMdHelp />
            </div>
        </div>
    </div>
  )
}
