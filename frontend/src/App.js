import { useState } from 'react';
import Editor from './components/inputs/Editor';
import './styles/App.css'
import { Route, Routes } from 'react-router-dom';
import CreatedPage from './pages/CreatedPage';
import Block from './pages/Block'

function App() {

  const [blocks, setBlocks] = useState(
    [
      {
        id: 1,
        text: 'text',
        short_url: 'short_url'

      }
    ])
  const [block, setBlock] = useState('')


  return (
    <Routes>
      <Route path="/" element={
        <div className="App">
          <Editor
            blocks={blocks}
            block={block}
            setBlock={setBlock}
            setBlocks={setBlocks}
          />
        </div>
      } />
      <Route path='/created' element={
        <CreatedPage></CreatedPage>
      }/>
      <Route path="/blocks/get/:hash_url" element={
        <Block></Block>
      } />
    </Routes>
  );
}

export default App;
