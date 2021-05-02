import React from 'react';
import Select from 'react-select';

class Informatik extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            sections: [],
            applicationSections: [],
            formElements: [],
            options: [],
            selectedAppl: "",
            applicationInputs: {},
            numbers: {}
        };
    }

    componentDidMount(){
        this.fetchJson();
    }

    fetchJson(){
        fetch('http://localhost:8000/informatik/')
            .then(res => res.json())
            .then(json => {
                let sections = [...json.sections];
                
                sections = sections.filter((el)=>{
                    return el.name !== "Anwendungsfach";
                });

                let applicationSections = json.sections.find(el => el.name === "Anwendungsfach").categories;
                const options = applicationSections.map((sect, i) => {
                    return { value: sect.id, label: sect.name };
                });
                this.setState({sections: sections, applicationSections: applicationSections, options: options});
                this.createForm();
            });
    }

    createForm(){
        let form = [];
        let applicationInputs = {};
        let sections = this.state.sections;
        let applicationSections = this.state.applicationSections;
        let numbers = {};

        // Create the Inputs for all basic subjects
        sections.forEach(section => {
            form.push(<h3 key={section.id}>{section.name}</h3>)
            section.subjects.forEach(subject => {
                numbers[subject.id] = 0;
                form.push(
                    <div id={subject.id+"-container"} key={subject.id+"-container"}>
                        <label htmlFor={subject.id}>{subject.name}</label>
                        <input
                            id={subject.id}
                            key={subject.id}
                            name={subject.name}
                            onChange={this.numberChange}
                            value={this.state.numbers[subject.id] === 0 ? "": this.state.numbers[subject.id]}
                            min="1"
                            max="5"
                            type="number"
                        />
                    </div>  
                );
            });
        });
        
        // create the Inputs for all application subjects
        applicationSections.forEach(section => { 
            let formArray = [];

            formArray.push(<h3 key={section.id}>{section.name}</h3>);

            section.subjects.forEach(subject => {
                numbers[subject.id] = 0;
                formArray.push(
                    <div id={subject.id+"-container"} key={subject.id+"-container"}>
                        <label htmlFor={subject.id}>{subject.name}</label>
                        <input
                            id={subject.id}
                            key={subject.id}
                            name={subject.name}
                            onChange={this.numberChange}
                            value={this.state.numbers[subject.id] === 0 ? "": this.state.numbers[subject.id]}
                            min="1"
                            max="5"
                            type="number"
                        />
                    </div>
                );
            });

            applicationInputs[section.id] = formArray;
        })

        this.setState({formElements: form, applicationInputs: applicationInputs});
    }

    selectApplication = (option) => {
        this.setState({selectedAppl: option.value});
    }

    numberChange = event => {
        let { value, min, max, id } = event.target;
        value = Math.max(Number(min), Math.min(Number(max), Number(value)));
        let numbers = this.state.numbers;
        numbers[id] = value;
        this.setState({ numbers: numbers });
    }

    handleSubmit = event => {
        if(this.state.selectedAppl){

            // create the object for the post request
            let postObj = {};

            this.state.sections.forEach(section => {
                let sectionObj = {};

                section.subjects.forEach(subject => {
                    let value = document.getElementById(subject.id).value;
                    if(value)
                        sectionObj[subject.id] = parseFloat(document.getElementById(subject.id).value);
                });

                postObj[section.id] = sectionObj;
            });

            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(postObj)
            };
            fetch('http://localhost:8000/informatik/', requestOptions)
                .then(response => response.json())
                .then(data => console.log(data));
        }
    }

    render() {
      return (
          <div className="container">
            <h3>Informatik</h3>
            {
                this.state.formElements.length > 0 ?
                <form>
                  {this.state.formElements}
                  {this.state.options && this.state.options.length ? 
                    <Select options={this.state.options} onChange={e => this.selectApplication(e)}/>
                    : <div></div>
                  }
                  {
                    this.state.selectedAppl !== "" ?
                    this.state.applicationInputs[this.state.selectedAppl]
                    : <div></div>
                  }
                  <input 
                    type="button"
                    value="Submit"
                    onClick={this.handleSubmit}
                  />
                </form> : <div></div>
            }
          </div>
      );
    }
}

export default Informatik;