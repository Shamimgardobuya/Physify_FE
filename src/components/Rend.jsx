import React , { useEffect, useRef } from "react";
import katex from "katex";

const Rend = (props)=> {
    const mathContainerRef = useRef(null);

    useEffect(()=> {
        if (mathContainerRef.current ) {
            katex.render(props.text, mathContainerRef.current, {
        throwOnError: false,
      });

        }
    }, [props.text])

    return (
        <>
       <div ref={mathContainerRef}></div>
        </>
    )
}

export default Rend;