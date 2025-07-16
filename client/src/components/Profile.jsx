import React from 'react'
import { RiSettings4Fill } from "react-icons/ri";

export const Profile = () => {
  const user = [
    {name: "Deepanshu1209", status:"online"}
  ]
  return (
    <div className='bg-[#202024] w-80 h-16 rounded-lg'>
        <div>
            <img src='' alt=''/>
            <div>
                {user.map((user, index)=>(
                    <div>
                        <span>{user.name}</span>
                        <span>{user.status}</span>
                    </div>
                ))}
            </div>
        </div>
        <div>
            <RiSettings4Fill color='white' /> 
        </div>
    </div>
  )
}
