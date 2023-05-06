import React from 'react'
import {Card} from './Card'
import styles from './Home.module.scss'
import logo from "../Assets/rizzify.png"


export default  function(): JSX.Element{
  const handleClick = (e) => {
    e.preventDefault();

  }
 

    return (
        <Card>
          <img className={styles.img} src = { logo} />
          <button className={styles.button2}onClick={handleClick}>
            Chat
          </button>

          <button className={styles.button}onClick={handleClick}>
            Next 
          </button>
        </Card>
    )
}