import React from 'react'

function Dashboard() {
    fetch("/dashboard", {
        method:"POST",
        cache: "no-cache",
        headers:{
            "content_type":"application/json",
        },
        body:JSON.stringify(this.state.value)
        }
    ).then(response => {

    return response.json()
  })
  .then(json => {

  this.setState({playerName: json[0]})
  })
  return (
      <div>
          Dashboard
      </div>
  )
}

export default Dashboard