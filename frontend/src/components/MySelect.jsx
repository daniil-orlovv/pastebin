import classes from './MySelect.module.css'

function MySelect({options, defaultValue, value, setSelect}) {
  return (
    <div className={classes.MySelect}>
        <select name="" id="" value={value} onChange={e => setSelect(e.target.value)}>
            {options.map(option =>
                <option key={option.value} value={option.value}>
                    {defaultValue} {option.name}
                </option>
            )}

        </select>
        
    </div>
  )
}

export default MySelect