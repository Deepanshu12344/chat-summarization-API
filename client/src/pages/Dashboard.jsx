import React from 'react'
import { Topbar } from '../components/Topbar'
import { Sidebar } from '../components/Sidebar'
import { Profile } from '../components/Profile'

export const Dashboard = () => {
  return (
    <div>
        <Topbar />
        <Sidebar />
        <span className='absolute bottom-[10px] left-[10px] z-50'> 
            <Profile />
        </span>
    </div>
  )
}
