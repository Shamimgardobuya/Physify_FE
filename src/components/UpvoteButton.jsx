import React, { use, useEffect, useRef, useState, useSyncExternalStore } from "react";
// import { HttpsProxyAgent } from "https-proxy-agent";
import WebSocket from 'ws';
import useWebSocket from 'react-use-websocket'
const UpvoteButton = (props) => {
    const [ count, setCount ] = useState(0)
    const[ dataFromSocket , setDataFromSocket ] = useState(null)
    const wsRef = useRef(null) 
        
    let websocket_url = `${process.env.REACT_APP_SOCKET_URL}`;
                
    const counter = () => {
        setCount(count + 1)
    
    }

    const { getWebSocket, readyState, sendJsonMessage , lastJsonMessage} = useWebSocket(websocket_url, {
                onOpen: () => {
                    console.log("connection established");
                    wsRef.current = getWebSocket()
                },
                onClose: () => {
                    console.log("Websocket connection closed");
                },
                onMessage: (event) => {
                    const data  = JSON.parse(event.data)
                    setDataFromSocket(data)
                },
                
                
            })
        useEffect (()=> {
            sendJsonMessage([props.answerId, count])
    
            
            return () => {
                if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
            
                    wsRef.current.close();
                }
                console.log('current',wsRef.current)
            }
        
            }, [count])
    

    
    

console.log('data from socket', dataFromSocket)
    return (
        <>
        <button className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold px-4 py-2" onClick={counter}> Upvote</button>
        <p>{dataFromSocket}</p>
        </>
    )
    
}

export default UpvoteButton;