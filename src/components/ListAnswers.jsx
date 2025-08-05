import React, { useEffect, useState } from "react";
import UpvoteButton from "./UpvoteButton";
import Rend from "./Rend";
import { useParams, Link } from "react-router-dom";

const Answers = ()=> {
    const { id } = useParams()
    const [answers, setAnswers] = useState([])
     useEffect(() => {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/questions/${id}`)
      .then(res => res.json())
      .then(data => setAnswers(data.data.answers) )
      .catch(err => console.error(err));
   
    
  }, [id]);

    return (
        <>
        <div>


<button data-drawer-target="default-sidebar" data-drawer-toggle="default-sidebar" aria-controls="default-sidebar" type="button" class="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
   <span className="sr-only">Open sidebar</span>
   <svg className="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
   <path clipRule-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
   </svg>
</button>

<aside id="default-sidebar" className="fixed top-0 left-0 z-40 w-129 h-screen transition-transform -translate-x-full sm:translate-x-0" aria-label="Sidebar">
   <div className="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
    <ul className="space-y-2 font-medium">

            { answers && answers?.map((answer) => 
                        <li key={answer.id} className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"> 
                        {
                            <Rend text={(answer.text)}/>
}                        <img src={answer.image_url} alt="none" className="w-40"/>


                        <UpvoteButton answerId={answer.id}/>
                    </li>
                    )}

      </ul>
      { !answers && 
                    <Link  className="p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"    to={`/answer/${id}`} >No answer yet, click to create one</Link>

      }

   </div>
</aside>

        </div>
        
        
        
        </>


    )

}

export default Answers