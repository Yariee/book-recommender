import { useState } from 'react';

export default function App() {
  const [bookTitle, setBookTitle] = useState('');
  const [messages, setMessages] = useState([]);
  const [response, setResponse] = useState('');
  const [isLoading, setLoading] = useState(false);

  function handleChange(e) {
    setBookTitle(e.target.value);
  }

  return (
    <>
      <input value={bookTitle} onChange={handleChange} />
      <button onClick={() => console.log(bookTitle)}>
        Submit
      </button>

      {isLoading && <p>Loading...</p>}
      {response && <p>{response}</p>}
    </>
  )
}

