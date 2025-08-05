import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import Rend from "./Rend";
import 'katex/dist/katex.min.css';
const ListQuestions = ()=> {
    const [questionsWithAnswers, setQuestionsWithAnswers ] = useState([])
    const [ prevPage, setPrevPage ] = useState([])
    const [ nextPage, setNextPage ] = useState([])

    const [loading, setLoading ] = useState(true)
    const navigate = useNavigate(null)
    const getQuestions = async() => {
            try {
                let data = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/questions?page=1`)
                setLoading(false)
                setQuestionsWithAnswers(data.data.data)
                setPrevPage(data.data.prev_page_data)
                setNextPage(data.data.next_page_data)

                
            }catch (error) {
                console.log(error)

            }
        }
    useEffect(()=> {
        const controller = new AbortController()
        
        getQuestions()
        return () => {
            controller.abort()
        }
    }, [])
    if (loading ){
        return <p>loading....</p>
    }

    return (
        <>
        <div>

            <ul className="space-y-4">
                {
                    questionsWithAnswers && questionsWithAnswers.length > 0 &&
                    questionsWithAnswers?.map(question => 
                        (
                        <li 
                            key={question.id}  className="p-4 border rounded-xl shadow-sm bg-white" > 
                        
                        <img src={question.image_url} alt="none" className="w-40"/>
                            <Rend text={question.text}/>
                            {console.log("uuu",  <Rend text={question.text}/> )}
                            <button className="text-sm text-blue-600 mt-2" onClick={()=> 
                                navigate(`${question.id}`)
                                
                                }>View answers</button>
                    </li>
                    ))
                }
                </ul>
                <Link  className="text-sm text-blue-600 mt-2 mx-4"  onClick={()=> ( nextPage && setQuestionsWithAnswers(nextPage))}> Next page </Link>
                <Link  className="text-sm text-blue-600 mt-2 mx-4"   onClick={()=> ( prevPage && setQuestionsWithAnswers(prevPage))}> Prev page </Link>


        </div>
        
        
        
        </>


    )

}

export default ListQuestions;