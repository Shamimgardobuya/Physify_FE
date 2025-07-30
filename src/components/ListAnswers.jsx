import React, { useEffect, useRef, useState } from "react";
import axios from "axios";
import UpvoteButton from "./UpvoteButton";
import Rend from "./Rend";

const Answers = ()=> {
    const [ answers, setAnswers ] = useState([])
    const getAnswers = async() => {
            try {
                let data = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/answers`)
                setAnswers(data.data.data)
                
            }catch (error) {
                console.log(error)

            }
        }

    useEffect(()=> {
        
        
        getAnswers()
    }, [])
    

    return (
        <>
        <div>

            <ul className="list-none">
                    {Object.keys(answers).map((objKey, i ) => 
                        <li key={crypto.randomUUID()} className="block w-full px-4 py-2 border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"> 
                        {
                            <Rend text={(JSON.stringify(answers[objKey].text))}/>
}
                        <UpvoteButton answerId={JSON.stringify(answers[objKey].id)}/>
                    </li>
                    )}
                </ul>


        </div>
        
        
        
        </>


    )

}

export default Answers