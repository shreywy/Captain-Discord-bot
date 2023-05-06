import React from 'react'
import { Route, Redirect, Switch } from 'wouter'




export default function App (): JSX.Element {
  return (
    <div>
        <input type="text" ref="myInput" />
        <input
          type="button"
          value="Alert the text input"
          onClick={this.handleClick}
        />
      </div>
  )
}
