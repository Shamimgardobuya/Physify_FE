import axios from "axios";
import {  useNavigate } from "react-router-dom";

const Login = () => {
    const navigate = useNavigate()
    const handleSubmitData = async(formData)=> {
        try {
            console.log('formdata',formData.get("password"),)
            let login_user = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/users?login=1`,
                {
                    name: formData.get("username"),
                    password: formData.get("password")
                },
                {
                    headers: {
                        "Content-Type" : "application/json"
                    }
                }
            );
            if (login_user) {
                console.log(login_user.data.data)

                localStorage.setItem("access_token", login_user.data.data)
                console.log("gong")
                navigate('/questions')


            }

        } catch (error) {
            console.log('error from loging in ',error)
        }

    }
    return (

        <>
          
<form class="max-w-sm mx-auto" action={handleSubmitData}>
  <div class="mb-5">
    <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your username</label>
    <input type="username" name="username" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com" required />
  </div>
  <div class="mb-5">
    <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
    <input type="password"  name="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
  </div>
  
  <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
</form>
        </>


    )
}
export default Login;