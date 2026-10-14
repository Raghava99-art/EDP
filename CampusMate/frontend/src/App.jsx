import { useEffect, useRef, useState } from 'react'

const API = 'http://127.0.0.1:8000/api'
const starter = {
  role: 'assistant',
  text: 'Hi! I’m CampusGuide AI. Ask me about admissions, scholarships, exams, placements, fees, or campus services.',
  suggestions: []
}

export default function App() {
  const [messages, setMessages] = useState([starter])
  const [question, setQuestion] = useState('')
  const [category, setCategory] = useState('')
  const [categories, setCategories] = useState(['Admissions', 'Scholarships', 'Examinations', 'Placements', 'Fees', 'Library', 'Hostel', 'Academics', 'IT Support'])
  const [busy, setBusy] = useState(false)
  const bottomRef = useRef(null)

  useEffect(() => {
    fetch(`${API}/categories`).then(r => r.ok ? r.json() : null)
      .then(data => { if (data?.categories?.length) setCategories(data.categories) })
      .catch(() => {})
  }, [])

  useEffect(() => bottomRef.current?.scrollIntoView({ behavior: 'smooth' }), [messages, busy])

  async function sendQuestion(value = question) {
    const q = value.trim()
    if (!q || busy) return
    setMessages(prev => [...prev, { role: 'user', text: q }])
    setQuestion('')
    setBusy(true)
    try {
      const response = await fetch(`${API}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q, category: category || null })
      })
      if (!response.ok) throw new Error('The server could not process your question.')
      const data = await response.json()
      setMessages(prev => [...prev, {
        role: 'assistant', text: data.answer, matched: data.matched,
        results: data.results || [], question: q
      }])
    } catch {
      setMessages(prev => [...prev, {
        role: 'assistant',
        text: 'I could not connect to the backend. Start the API at http://127.0.0.1:8000 and try again.',
        results: []
      }])
    } finally {
      setBusy(false)
    }
  }

  async function sendFeedback(message, helpful) {
    const first = message.results?.[0]
    if (!first || !message.question) return
    try {
      await fetch(`${API}/feedback`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: message.question, faq_id: first.id, helpful })
      })
      setMessages(prev => prev.map(m => m === message ? { ...m, feedbackSent: true } : m))
    } catch { /* Feedback is optional if API is offline. */ }
  }

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand-mark">C<span>G</span></div>
        <div>
          <div className="brand-name">CampusGuide <b>AI</b></div>
          <div className="brand-subtitle">STUDENT HELP DESK</div>
        </div>
        <div className="side-divider" />
        <p className="side-label">QUICK TOPICS</p>
        {['Admissions', 'Scholarships', 'Examinations', 'Placements', 'Fees', 'Library'].map(item =>
          <button key={item} className={`topic ${category === item ? 'selected' : ''}`}
            onClick={() => setCategory(category === item ? '' : item)}>
            <span className="topic-dot" />{item}
          </button>
        )}
        <div className="sidebar-bottom">
          <div className="status-dot" /> Local FAQ assistant
          <p>Answers are based on the sample FAQ dataset.</p>
        </div>
      </aside>

      <main className="main-panel">
        <header className="topbar">
          <div><div className="eyebrow">YOUR CAMPUS, SIMPLIFIED</div><h1>Student Helpdesk</h1></div>
          <div className="online-pill"><span /> AI assistant online</div>
        </header>

        <section className="welcome">
          <div className="welcome-icon">✦</div>
          <div>
            <h2>What can I help you find?</h2>
            <p>Ask a question in your own words. I’ll look for the closest match in the college FAQ.</p>
          </div>
        </section>

        <div className="filter-row">
          <span>SEARCHING</span>
          <select value={category} onChange={e => setCategory(e.target.value)}>
            <option value="">All topics</option>
            {categories.map(c => <option key={c} value={c}>{c}</option>)}
          </select>
          {category && <button className="clear-filter" onClick={() => setCategory('')}>Clear filter ×</button>}
        </div>

        <section className="chat-area" aria-live="polite">
          {messages.map((message, index) => (
            <div className={`message-row ${message.role}`} key={index}>
              {message.role === 'assistant' && <div className="avatar">✦</div>}
              <div className="message-content">
                <div className="message-meta">{message.role === 'assistant' ? 'CAMPUSGUIDE AI' : 'YOU'}</div>
                <div className={`bubble ${message.role}`}>{message.text}</div>
                {message.results?.length > 0 && (
                  <div className="matches">
                    <div className="matches-heading">RELATED FAQ MATCHES</div>
                    {message.results.map(result => (
                      <div className="match-card" key={result.id}>
                        <div><span className="match-category">{result.category}</span><p>{result.question}</p></div>
                        <span className="score">{Math.round(result.similarity * 100)}%</span>
                      </div>
                    ))}
                  </div>
                )}
                {message.role === 'assistant' && message.results?.length > 0 && (
                  <div className="feedback-row">
                    {message.feedbackSent ? <span className="feedback-thanks">Thanks for the feedback!</span> : <>
                      <span>Was this helpful?</span>
                      <button onClick={() => sendFeedback(message, true)} aria-label="Helpful">👍</button>
                      <button onClick={() => sendFeedback(message, false)} aria-label="Not helpful">👎</button>
                    </>}
                  </div>
                )}
              </div>
            </div>
          ))}
          {busy && <div className="typing"><span /><span /><span /> Searching FAQs…</div>}
          <div ref={bottomRef} />
        </section>

        <div className="composer-wrap">
          <div className="suggestion-row">
            {['How do I apply for a scholarship?', 'Where is the exam timetable?', 'How do placements work?'].map(s =>
              <button key={s} onClick={() => sendQuestion(s)} disabled={busy}>{s}</button>
            )}
          </div>
          <form className="composer" onSubmit={e => { e.preventDefault(); sendQuestion() }}>
            <input value={question} onChange={e => setQuestion(e.target.value)}
              placeholder="Ask anything about your college…" maxLength={500} />
            <button type="submit" disabled={busy || !question.trim()}>Send <span>↗</span></button>
          </form>
          <p className="disclaimer">CampusGuide AI can be wrong. Verify important information with official college sources.</p>
        </div>
      </main>
    </div>
  )
}
