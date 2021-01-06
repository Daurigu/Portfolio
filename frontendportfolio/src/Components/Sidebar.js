import React from 'react'

function Sidebar(){
    return(
        <div className='col-2 wrapper'>
            <ul>
                <h1 className='text-white mt-5 mb-5'>Daniel</h1>
                <li className='list-unstyled mt-3'>
                    <a href='google.com' className='btn btn-outline-success '>Home</a>
                </li>
                <li className='list-unstyled mt-3'>
                    <a href='google.com' className='btn btn-outline-success '>Tech</a>
                </li>
                <li className='list-unstyled mt-3'>
                    <a href='google.com' className='btn btn-outline-success '>Creative</a>
                </li>
                <li className='list-unstyled mt-3'>
                <a href='google.com' className='btn btn-outline-success '>Cert</a>
                </li>

            </ul>
        </div>
    )
}

export default Sidebar