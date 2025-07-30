import React, { useEffect, useRef, useState } from "react";
import axios from "axios";


const ListQuestions = ()=> {
    const [questionsWithAnswers, setQuestionsWithAnswers ] = useState([])
    const getQuestions = async() => {
            try {
                let data = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/questions`)
                setQuestionsWithAnswers(data.data.data)
                
            }catch (error) {
                console.log(error)

            }
        }

    useEffect(()=> {
        
        
        getQuestions()
    }, [])
    

    return (
        <>
        <div>

              <ul className="list-none">
                    {JSON.stringify(questionsWithAnswers)}
                </ul>


        </div>
        
        
        
        </>


    )

}

export default ListQuestions;