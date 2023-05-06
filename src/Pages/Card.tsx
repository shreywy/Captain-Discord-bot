import React from  'react'
import styles from './Card.module.scss'






export function Card ({
    children
  }: {
    children: React.ReactNode
   
  }): JSX.Element {
    return (
        <div className= {styles.card}>
        <div> {children} </div>
    </div>
      
    )
  }