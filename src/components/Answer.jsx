import { useRef } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router";
const Answer = () => {
  
  const formRef = useRef();
  const navigate = useNavigate()
  const { question_id } = useParams()
  const submitData =  async(formData)=> {
    try {
      console.log(formData.get('file'))
      console.log(question_id, formData.get('file'));
      let data = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/answers`, 
        {file : formData.get('file'), 
          question_id : formData.get('question_id')
        }
      
    ,{
      headers :{ 
       ' Authorization' : `Bearer ${localStorage.getItem('access_token')}`,
       'Content-Type' : 'multipart/form-data'
      }
      
    })
    if(data.data) {
      navigate(`/questions/${question_id}`)

    }

    } catch (error) {
      console.log(error
      )
    }
  }
    return (
        <div>


<form  class="max-w-sm mx-auto" encType="multipart/form-data" action={submitData}>
  
  <div class="mb-5">
    <label for="image" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Upload image</label>
    <input type="file" name="file" id="file" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
    <input type="text" hidden value={question_id} name="question_id" />
  </div>
  <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
</form>

        </div>

    )
}



export default Answer;