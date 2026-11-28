import React, {useEffect, useMemo, useState} from 'react'
import {createRoot} from 'react-dom/client'
import {
    Activity, ArrowDownRight, ArrowUpRight, Bell, BriefcaseBusiness, Building2,
    ChevronDown, ChevronLeft, ChevronRight, CircleHelp, Command, FileText,
    LayoutDashboard, LogOut, Menu, Search, Settings2, ShieldCheck, Users, X,
} from 'lucide-react'
import './styles.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/company/'
const PAGE_SIZE = 25
const sections = [
    {id: 'dashboard', label: 'Огляд', icon: LayoutDashboard},
    {id: 'employees', label: 'Команда', icon: Users},
    {id: 'projects', label: 'Проєкти', icon: BriefcaseBusiness},
    {id: 'clients', label: 'Клієнти', icon: Building2},
    {id: 'contracts', label: 'Договори', icon: FileText},
]
const seed = {
    company: {name: 'ZemNyux Inc.', tagline: 'Простір компанії'},
    departments: [], employees: [], projects: [], clients: [], contracts: [], meta: {total: 0},
}
const formats = {
    employees: {
        title: 'Команда',
        caption: 'Усі працівники компанії',
        icon: Users,
        search: 'Знайти працівника…',
        cols: ['Працівник', 'Відділ', 'Посада', 'Контакт']
    },
    projects: {
        title: 'Проєкти',
        caption: 'Стежте за прогресом активних проєктів',
        icon: BriefcaseBusiness,
        search: 'Знайти проєкт…',
        cols: ['Проєкт', 'Код', 'Статус', 'Бюджет', 'Початок']
    },
    clients: {
        title: 'Клієнти',
        caption: 'Клієнтська база та партнерства',
        icon: Building2,
        search: 'Знайти клієнта…',
        cols: ['Клієнт', 'Галузь', 'Країна', 'Email', 'Статус']
    },
    contracts: {
        title: 'Договори',
        caption: 'Підписані угоди та фінансова інформація',
        icon: FileText,
        search: 'Знайти договір…',
        cols: ['Договір', 'Клієнт', 'Сума', 'Дата підписання']
    },
}
const initials = (name = '') => name.split(/\s+/).filter(Boolean).slice(0, 2).map((part) => part[0]).join('').toUpperCase()
const money = (value) => new Intl.NumberFormat('uk-UA', {
    style: 'currency',
    currency: 'EUR',
    maximumFractionDigits: 0
}).format(Number(value || 0))
const date = (value) => value ? new Intl.DateTimeFormat('uk-UA', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
}).format(new Date(`${value}T12:00:00`)) : '—'

function App() {
    const [data, setData] = useState(seed)
    const [connection, setConnection] = useState('loading')
    const [active, setActive] = useState('dashboard')
    const [query, setQuery] = useState('')
    const [menuOpen, setMenuOpen] = useState(false)
    const [profileOpen, setProfileOpen] = useState(false)
    const [toast, setToast] = useState('')

    const loadData = async () => {
        setConnection('loading')
        try {
            const response = await fetch(API_URL, {headers: {Accept: 'application/json'}})
            if (!response.ok) throw new Error(`HTTP ${response.status}`)
            const payload = await response.json()
            setData({...seed, ...payload})
            setConnection('connected')
            setToast('З’єднання з Django-сервером оновлено')
        } catch {
            setConnection('offline')
            setToast('Не вдалося з’єднатись. Перевірте, чи запущений Django на localhost:8000.')
        }
        window.setTimeout(() => setToast(''), 4200)
    }
    useEffect(() => {
        loadData()
    }, [])

    const counts = {
        departments: data.departments.length,
        employees: data.employees.length,
        projects: data.projects.length,
        clients: data.clients.length,
        contracts: data.contracts.length,
        activeProjects: data.projects.filter((item) => item.status === 'active').length,
    }
    const allRows = data[active] || []
    const filteredRows = useMemo(() => allRows.filter((row) => Object.values(row).join(' ').toLocaleLowerCase('uk').includes(query.toLocaleLowerCase('uk'))), [allRows, query])

    const openSection = (id) => {
        setActive(id);
        setQuery('');
        setMenuOpen(false)
    }

    return (
        <div className="app-shell">
            <aside className={`sidebar ${menuOpen ? 'sidebar-open' : ''}`}>
                <div className="brand">
                    <div className="brand-mark">z<span>.</span></div>
                    <div className="brand-copy"><strong>ZemNyux</strong><span>WORKSPACE</span></div>
                    <button className="mobile-close icon-button" onClick={() => setMenuOpen(false)}
                            aria-label="Закрити меню"><X size={17}/></button>
                </div>
                <button className="workspace-switch">
                    <div className="workspace-avatar">Z</div>
                    <span><strong>ZemNyux Inc.</strong><small>Головний простір</small></span><ChevronDown size={15}/>
                </button>
                <div className="nav-label">РОБОЧИЙ ПРОСТІР</div>
                <nav className="navigation" aria-label="Основна навігація">
                    {sections.map(({id, label, icon: Icon}) => <button key={id}
                                                                       className={`nav-item ${active === id ? 'selected' : ''}`}
                                                                       onClick={() => openSection(id)}><Icon size={17}/><span>{label}</span>{id === 'projects' && counts.activeProjects > 0 &&
                        <span className="nav-count">{counts.activeProjects}</span>}</button>)}
                </nav>
                <div className="nav-label secondary-label">НАЛАШТУВАННЯ</div>
                <nav className="navigation">
                    <button className="nav-item"
                            onClick={() => setToast('Дані завантажуються безпосередньо з Django API.')}><Settings2
                        size={17}/><span>Налаштування</span></button>
                    <button className="nav-item" onClick={() => setToast('ZemNyux — внутрішній простір команди.')}>
                        <CircleHelp size={17}/><span>Довідка</span></button>
                </nav>
                <div className="sidebar-bottom">
                    <div className="plan-card">
                        <div className="plan-icon"><ShieldCheck size={15}/></div>
                        <div className="plan-heading"><span>Захищений простір</span><span className="plan-dot"/></div>
                        <p>Дані підключені до локальної бази компанії.</p>
                        <div className="plan-footer"><span>ЛОКАЛЬНЕ З’ЄДНАННЯ</span><span>●</span></div>
                    </div>
                    <div className="profile-wrap">
                        <button className="profile" onClick={() => setProfileOpen(!profileOpen)}>
                            <div className="avatar avatar-profile">М</div>
                            <span><strong>Мій профіль</strong><small>Адміністратор</small></span><ChevronDown
                            size={15}/></button>
                        {profileOpen && <div className="profile-menu"><span className="profile-email">Локальний робочий простір</span>
                            <button onClick={() => {
                                setProfileOpen(false);
                                setToast('Сесія адміністратора активна.')
                            }}><LogOut size={14}/>Статус сесії
                            </button>
                        </div>}</div>
                </div>
            </aside>
            {menuOpen &&
                <button className="mobile-backdrop" onClick={() => setMenuOpen(false)} aria-label="Закрити меню"/>}
            <main className="main-area">
                <header className="topbar">
                    <div className="topbar-left">
                        <button className="mobile-menu icon-button" onClick={() => setMenuOpen(true)}
                                aria-label="Відкрити меню"><Menu size={19}/></button>
                        <div className="breadcrumbs"><span>Простір</span><ChevronRight
                            size={14}/><strong>{sections.find((section) => section.id === active)?.label}</strong></div>
                    </div>
                    <div className="topbar-right"><span className="connection-pill"><i
                        className={connection}/>{connection === 'connected' ? 'Django підключено' : connection === 'loading' ? 'З’єднання…' : 'Немає з’єднання'}</span>
                        <button className="icon-button refresh-button" onClick={loadData} title="Оновити дані"
                                aria-label="Оновити дані"><Activity size={17}/></button>
                        <button className="icon-button bell-button" aria-label="Сповіщення"
                                onClick={() => setToast('Наразі нових сповіщень немає.')}><Bell size={17}/><i/></button>
                        <div className="top-avatar">М</div>
                    </div>
                </header>
                <div className="page-content">
                    {active === 'dashboard' ?
                        <Dashboard data={data} counts={counts} connection={connection} onNavigate={openSection}/> :
                        <DataSection key={active} kind={active} rows={filteredRows} query={query} onQuery={setQuery}/>}
                    <footer className="page-footer"><span>© 2026 {data.company.name} · Внутрішній портал</span><span
                        className="footer-right"><span className="footer-signal"/> API <code>/api/company/</code></span>
                    </footer>
                </div>
            </main>
            {toast && <div className="toast"><span className="toast-icon"><Command size={15}/></span>{toast}</div>}
        </div>
    )
}

function Dashboard({data, counts, connection, onNavigate}) {
    const stats = [
        {
            name: 'Працівники',
            value: counts.employees,
            change: `${counts.departments} відділи`,
            icon: Users,
            color: 'blue',
            target: 'employees'
        },
        {
            name: 'Активні проєкти',
            value: counts.activeProjects,
            change: `${counts.projects} загалом`,
            icon: BriefcaseBusiness,
            color: 'amber',
            target: 'projects'
        },
        {
            name: 'Клієнти',
            value: counts.clients,
            change: 'У базі компанії',
            icon: Building2,
            color: 'green',
            target: 'clients'
        },
        {
            name: 'Договори',
            value: counts.contracts,
            change: 'У реєстрі',
            icon: FileText,
            color: 'violet',
            target: 'contracts'
        },
    ]
    return <>
        <section className="welcome-row">
            <div>
                <div className="eyebrow"><span/>ПОНЕДІЛОК, 21 ЛИСТОПАДА 2026</div>
                <h1>Простір компанії<span>.</span></h1><p>З поверненням. Ось що відбувається у {data.company.name}.</p>
            </div>
            <div className="welcome-actions">
                <button className="today-button"><span className="calendar-icon">▦</span> Огляд за сьогодні <ChevronDown
                    size={14}/></button>
            </div>
        </section>
        <section className="hero-card">
            <div className="hero-orb orb-one"/>
            <div className="hero-orb orb-two"/>
            <div className="hero-grid"/>
            <div className="hero-content">
                <div className="hero-kicker"><span className="sparkle">✳</span> {data.company.name.toUpperCase()}</div>
                <h2>Створюємо<br/>майбутнє разом.</h2><p>Один простір для людей, проєктів та ідей, що рухають нас
                вперед.</p>
                <div className="hero-actions">
                    <button className="hero-button" onClick={() => onNavigate('projects')}>Переглянути
                        проєкти <ArrowUpRight size={15}/></button>
                    <span className="hero-meta">ОНОВЛЕНО З БАЗИ ДАНИХ</span></div>
            </div>
            <div className="hero-illustration" aria-hidden="true">
                <div className="illustration-ring ring-back"/>
                <div className="illustration-ring ring-mid"/>
                <div className="illustration-ring ring-front"/>
                <div className="illustration-core">z.</div>
                <div className="orbit-dot dot-a"/>
                <div className="orbit-dot dot-b"/>
                <div className="orbit-dot dot-c"/>
                <div className="orbit-chip chip-top"><Activity size={13}/><span>У фокусі</span></div>
                <div className="orbit-chip chip-bottom"><span className="chip-live"/>{counts.activeProjects} активних
                    проєктів
                </div>
            </div>
            <div className="hero-index">01 — 04</div>
        </section>
        <section className="stats-grid">{stats.map(({name, value, change, icon: Icon, color, target}) => <button
            className="stat-card" key={name} onClick={() => onNavigate(target)}>
            <div className="stat-top"><span>{name}</span><span className={`stat-icon ${color}`}><Icon size={17}/></span>
            </div>
            <div className="stat-value">{value}<span className={`trend ${value ? '' : 'muted-trend'}`}>{value ?
                <ArrowUpRight size={13}/> : <ArrowDownRight size={13}/>}{value ? ' активність' : ' оновлень'}</span>
            </div>
            <div className="stat-bottom"><span>{change}</span><span className="stat-arrow"><ArrowUpRight
                size={14}/></span></div>
        </button>)}</section>
        <section className="lower-grid">
            <div className="panel activity-panel">
                <div className="panel-header">
                    <div><h3>Команда</h3><p>Люди, що створюють результат</p></div>
                    <button className="text-action" onClick={() => onNavigate('employees')}>Вся команда <ArrowUpRight
                        size={14}/></button>
                </div>
                {data.employees.length ?
                    <div className="team-list">{data.employees.slice(0, 5).map((person, index) => <div
                        className="team-row" key={person.id}>
                        <div className={`avatar team-avatar av-${index % 5}`}>{initials(person.full_name)}</div>
                        <div className="person-main"><strong>{person.full_name}</strong><span>{person.position}</span>
                        </div>
                        <span className="department-pill">{person['department__name']}</span><a className="mail-icon"
                                                                                                href={`mailto:${person.email}`}
                                                                                                aria-label={`Написати ${person.full_name}`}><ArrowUpRight
                        size={15}/></a></div>)}</div> :
                    <EmptyInline connected={connection === 'connected'} text="У базі ще немає записів працівників."/>}
                <div className="panel-foot"><span><span
                    className="live-dot"/> {connection === 'connected' ? 'Синхронізовано з Django' : 'Підключаємося до сервера'}</span><span>{counts.employees} записів</span>
                </div>
            </div>
            <div className="panel projects-panel">
                <div className="panel-header">
                    <div><h3>Проєкти</h3><p>Останні оновлення</p></div>
                    <button className="more-button" onClick={() => onNavigate('projects')}
                            aria-label="Переглянути всі проєкти"><ChevronRight size={17}/></button>
                </div>
                {data.projects.length ?
                    <div className="project-list">{data.projects.slice(0, 4).map((project, index) => <div
                        className="project-row" key={project.id}>
                        <div className={`project-icon pi-${index % 4}`}><BriefcaseBusiness size={16}/></div>
                        <div className="project-main">
                            <strong>{project.title}</strong><span>{project.code} · {date(project.start_date)}</span>
                        </div>
                        <span className={`status-tag status-${project.status}`}>{statusLabel(project.status)}</span>
                    </div>)}</div> :
                    <EmptyInline connected={connection === 'connected'} text="У базі ще немає записів проєктів."/>}
                <div className="panel-foot"><span><span
                    className="live-dot"/> {counts.activeProjects} активних зараз</span>
                    <button className="panel-foot-link" onClick={() => onNavigate('projects')}>Відкрити <ArrowUpRight
                        size={13}/></button>
                </div>
            </div>
        </section>
        <div className="connection-note">
            <div className={`connection-indicator ${connection}`}><Activity size={15}/></div>
            <div><strong>Дані з робочого
                простору</strong><span>{connection === 'connected' ? `${data.meta.total} записів · оновлено щойно з локального Django API` : connection === 'loading' ? 'Отримуємо дані з локального Django API…' : 'Немає відповіді від сервера. Переконайтесь, що Django запущений.'}</span>
            </div>
            <span className="api-method">GET</span><code>localhost:8000/api/company/</code></div>
    </>
}

function statusLabel(status) {
    return ({active: 'В роботі', planned: 'Заплановано', done: 'Завершено', paused: 'Пауза'})[status] || status
}

function EmptyInline({connected, text}) {
    return <div className="empty-inline">
        <div className="empty-mark">{connected ? '○' : '↗'}</div>
        <strong>{text}</strong></div>
}

function DataSection({kind, rows, query, onQuery}) {
    const [currentPage, setCurrentPage] = useState(1)
    const cfg = formats[kind]
    const Icon = cfg.icon
    const pageCount = Math.max(1, Math.ceil(rows.length / PAGE_SIZE))
    const page = Math.min(currentPage, pageCount)
    const firstRow = rows.length ? (page - 1) * PAGE_SIZE + 1 : 0
    const lastRow = Math.min(page * PAGE_SIZE, rows.length)
    const visibleRows = rows.slice(firstRow - 1, lastRow)
    const pageWindowStart = Math.max(1, Math.min(page - 2, pageCount - 4))
    const pageWindowEnd = Math.min(pageCount, pageWindowStart + 4)
    const pageNumbers = Array.from(
        {length: pageWindowEnd - pageWindowStart + 1},
        (_, index) => pageWindowStart + index,
    )

    useEffect(() => {
        setCurrentPage(1)
    }, [kind, query])

    const exportRows = () => {
        const blob = new Blob([JSON.stringify(rows, null, 2)], {type: 'application/json'})
        const link = document.createElement('a')
        link.href = URL.createObjectURL(blob)
        link.download = `${kind}.json`
        link.click()
        URL.revokeObjectURL(link.href)
    }

    return (
        <section className="data-page">
            <div className="data-heading">
                <div>
                    <div className="eyebrow"><span/>РОБОЧИЙ ПРОСТІР / РЕЄСТР</div>
                    <h1>{cfg.title}<span>.</span></h1>
                    <p>{cfg.caption}</p>
                </div>
                <button className="export-button" onClick={exportRows}>
                    <ArrowDownRight size={15}/> Експортувати JSON
                </button>
            </div>

            <div className="data-controls">
                <div className="data-count">
                    <span className="count-icon"><Icon size={16}/></span>
                    <strong>{rows.length}</strong>
                    <span>записів у реєстрі</span>
                </div>
                <label className="search-field">
                    <Search size={15}/>
                    <input value={query} onChange={(event) => onQuery(event.target.value)} placeholder={cfg.search}/>
                    <kbd>⌘ K</kbd>
                </label>
            </div>

            <div className="table-panel">
                <div className="table-wrap">
                    <table>
                        <thead>
                        <tr>{cfg.cols.map((col) => <th key={col}>{col}</th>)}</tr>
                        </thead>
                        <tbody>{visibleRows.map((row) => <DataRow key={row.id} kind={kind} row={row}/>)}</tbody>
                    </table>
                    {rows.length === 0 && (
                        <div className="table-empty">
                            <div className="empty-illustration"><Icon size={24}/></div>
                            <strong>{query ? 'Нічого не знайдено' : 'Тут поки немає записів'}</strong>
                            <span>{query ? 'Спробуйте змінити пошуковий запит.' : 'Додайте дані у Django адмінпанелі, щоб побачити їх тут.'}</span>
                        </div>
                    )}
                </div>

                <div className="table-footer">
                    <span>Показано <strong>{firstRow}–{lastRow}</strong> із <strong>{rows.length}</strong> записів</span>
                    <nav className="pagination" aria-label="Сторінки реєстру">
                        <button type="button" disabled={page <= 1} onClick={() => setCurrentPage(page - 1)}
                                aria-label="Попередня сторінка">
                            <ChevronLeft size={15}/>
                        </button>
                        {pageNumbers.map((number) => (
                            <button
                                type="button"
                                key={number}
                                className={number === page ? 'page-current' : 'page-button'}
                                aria-label={`Сторінка ${number}`}
                                aria-current={number === page ? 'page' : undefined}
                                onClick={() => setCurrentPage(number)}
                            >
                                {number}
                            </button>
                        ))}
                        <button type="button" disabled={page >= pageCount} onClick={() => setCurrentPage(page + 1)}
                                aria-label="Наступна сторінка">
                            <ChevronRight size={15}/>
                        </button>
                    </nav>
                </div>
            </div>
        </section>
    )
}

function DataRow({kind, row}) {
    if (kind === 'employees') return <tr>
        <td>
            <div className="table-person">
                <div className="avatar table-avatar">{initials(row.full_name)}</div>
                <div><strong>{row.full_name}</strong><span>ID-{String(row.id).padStart(3, '0')}</span></div>
            </div>
        </td>
        <td><span className="table-muted">{row['department__name']}</span></td>
        <td>{row.position}</td>
        <td><a className="table-link" href={`mailto:${row.email}`}>{row.email}</a><span
            className="subline">{row.phone}</span></td>
    </tr>
    if (kind === 'projects') return <tr>
        <td>
            <div className="table-title"><span className="table-record-icon project-record"><BriefcaseBusiness
                size={15}/></span><strong>{row.title}</strong></div>
        </td>
        <td><code className="code-badge">{row.code}</code></td>
        <td><span className={`status-tag status-${row.status}`}>{statusLabel(row.status)}</span></td>
        <td>{money(row.budget)}</td>
        <td className="table-muted">{date(row.start_date)}</td>
    </tr>
    if (kind === 'clients') return <tr>
        <td>
            <div className="table-person">
                <div className="avatar client-avatar">{initials(row.name)}</div>
                <div><strong>{row.name}</strong><span>ID-{String(row.id).padStart(3, '0')}</span></div>
            </div>
        </td>
        <td>{row.industry}</td>
        <td className="table-muted">{row.country}</td>
        <td><a className="table-link" href={`mailto:${row.contact_email}`}>{row.contact_email}</a></td>
        <td><span
            className={`status-tag ${row.is_active ? 'status-active' : 'status-paused'}`}>{row.is_active ? 'Активний' : 'Неактивний'}</span>
        </td>
    </tr>
    return <tr>
        <td>
            <div className="table-title"><span className="table-record-icon contract-record"><FileText
                size={15}/></span>
                <div><strong>{row.title}</strong><span className="subline"><code>{row.number}</code></span></div>
            </div>
        </td>
        <td>{row['client__name']}</td>
        <td><strong>{money(row.amount)}</strong></td>
        <td className="table-muted">{date(row.signed_on)}</td>
    </tr>
}

createRoot(document.getElementById('root')).render(<React.StrictMode><App/></React.StrictMode>)
