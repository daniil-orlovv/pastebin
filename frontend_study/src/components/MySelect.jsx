import React from 'react'

const MySelect = ({options, defaultValue, value, onChange}) => {
  return (
    <div>
        <select
            value={value}
            onChange={e => onChange(e.target.value)}
        >
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