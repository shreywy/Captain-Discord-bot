import React from 'react'
import pw from './PageWrapper.module.scss'


export function PageWrapper ({
  children,
  pageTheme
}: {
  children: React.ReactNode
  pageTheme: string
}): JSX.Element {
  return (

    <div className={`${pw.container} ${pw[pageTheme]} ${pw[`background-${pageTheme}`]} `}>
      <div>
          {children}
        </div>
    </div>
  )
}
