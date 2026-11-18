import React from 'react'
import { useLocation, Navigate, Link } from 'react-router-dom'
import classes from './CreatedPage.module.css'

function CreatedPage() {
    const { state } = useLocation();

    if (!state?.url) return <Navigate to="/" replace />;

  return (
    <div className={classes.CreatedPage}>
        <h1 className={classes.CreatedPage__h1}>Блок создан</h1>
            <div className={classes.CreatedPage__url}>
            <p>
               Ссылка на блок: <a href={state.url} target='_blank' rel='noopener noreferer'>
                ссылка
            </a>
            </p>
            </div>
            <div className={classes.CreatedPage__btns}>
                <button>
                    <Link to={`/blocks/get/${state.url}`}>Перейти к блоку</Link>

                </button>
                <button onClick={() => navigator.clipboard.writeText(state.url)}>
                    Копировать
                </button>
                <button>
                    <Link to="/">Создать еще</Link>
                </button>
            </div>
        </div>
  );
}

export default CreatedPage