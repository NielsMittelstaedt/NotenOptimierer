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
            selectedAppl: ""
        };
    }

    componentDidMount(){
        this.fetchJson();
    }

    fetchJson(){
        fetch('http://localhost:8000/informatik')
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
        let sections = this.state.sections;

        // Create the Inputs for all basic subjects
        sections.forEach(section => {
            form.push(<h3 key={section.name}>{section.name}</h3>)
            section.subjects.forEach(subject => {
                form.push(
                    <div id={subject.id+"-container"} key={subject.id+"-container"}>
                        <label htmlFor={subject.id}>{subject.name}</label>
                        <input
                            id={subject.id}
                            key={subject.id}
                            name={subject.name}
                            type="number"
                        />
                    </div>  
                );
            });
        });
        
        // create the Inputs for all application subjects
        

        this.setState({formElements: form});
    }

    selectApplication(selectedOption) {
        this.setState({
            selectedAppl: selectedOption
        });
    }

    render() {
      return (
          <div className="container">
            <h3>Informatik</h3>
            {
                this.state.formElements.length > 0 ?
                <form >
                  {this.state.formElements}
                  {this.state.options && this.state.options.length ? 
                    <Select options={this.state.options} onChange={this.selectApplication}/>
                    : <div></div>
                  }
                  {
                    this.state.selectedAppl !== "" ?
                    this.state.
                  }
                  <input 
                    type="button"
                    value="Submit"
                  />
                </form> : <div></div>
            }
          </div>
          
      );
    }
}

export default Informatik;