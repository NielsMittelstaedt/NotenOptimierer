import React, { useState } from 'react';
 
function GradeForm() {
    const [allGrades, setAllGrades] = useState({
        progra: "0",
        dsal: "0",
        swt: "0",
        dbis: "0",

        ti: "0",
        bus: "0",
        datkom: "0",

        fosap: "0",
        buk: "0",
        malo: "0",

        ds: "0",
        la: "0",
        afi: "0",
        stoch: "0",

        pros: "0",
        sem: "0",

        wahl1: "0",
        wahl2: "0",
        wahl3: "0",
        wahl4: "0",

        ebwl: "0",
        qm: "0",
        elehre: "0",
        birw: "0"
    });
    
    function () {
        
    }

    const inputs = []

    for (const [key, value] of Object.entries(allGrades)){
        inputs.push(
            <input
                id={key}
                name={key}
                key={key}
                type="number"
                value={value === 0 ? "" : value}
                onChange={(e) => {
                    setAllGrades((prevGrades) => {
                        return { ...prevGrades, [e.target.name]: e.target.value};
                    });
                }}
            />
        );
    }

    return (
    <form >
        {inputs}
        <input 
            type="button"
            value="Submit"
            onClick={printObject}
        />
    </form>
    )
}
 
export default GradeForm;