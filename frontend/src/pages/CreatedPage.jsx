import React from 'react'
import { useLocation, Navigate, useNavigate } from 'react-router-dom'
import classes from './CreatedPage.module.css'

function CreatedPage() {
    const { state } = useLocation();
    const navigate = useNavigate();

    if (!state?.hash_id) return <Navigate to="/" replace />;

    const path = `/${state.hash_id}`;
    const fullUrl = `${window.location.origin}${path}`;

    return (
        <div className={classes.CreatedPage}>
            <h1 className={classes.CreatedPage__h1}>Блок создан</h1>
                <div className={classes.CreatedPage__url}>
                <p>
                    Ссылка на блок:{' '}
                    <a href={fullUrl} target='_blank' rel='noopener noreferrer'>
                        {fullUrl}
                    </a>
                </p>
                </div>
                <div className={classes.CreatedPage__btns}>
                    <button onClick={() => navigate(path)}>Перейти к блоку</button>
                    <button onClick={() => navigator.clipboard.writeText(fullUrl)}>
                    Копировать
                    </button>
                    <button onClick={() => navigate('/')}>Создать еще</button>
                </div>
            </div>
    );
}

export default CreatedPage