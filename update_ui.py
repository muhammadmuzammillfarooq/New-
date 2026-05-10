from pathlib import Path

files = {
    'src/pages/Home.jsx': '''import Navbar from "../components/Navbar.jsx";
import Hero from "../components/Hero.jsx";
import Work from "../components/Work.jsx";
import Skill from "../components/Skill.jsx";
import About from "../components/About.jsx";
import Contact from "../components/Contact.jsx";

const Home = () => {
  return (
    <div className="bg-slate-50 text-slate-900">
      <Navbar />
      <Hero />
      <About />
      <Work />
      <Skill />
      <Contact />
    </div>
  );
};

export default Home;
''',
    'src/components/Hero.jsx': '''import { FaArrowRight } from "react-icons/fa";
import { assets } from "../assets.js";

const Hero = () => {
  return (
    <section id="home" className="min-h-screen bg-gradient-to-br from-slate-50 via-slate-100 to-white flex items-center pt-24">
      <div className="max-w-7xl mx-auto px-6 py-20">
        <div className="grid grid-cols-1 gap-12 lg:grid-cols-2 items-center">
          <div className="text-center lg:text-left">
            <p className="mb-4 text-sm uppercase tracking-[0.3em] text-teal-700 font-semibold">Frontend Web Developer</p>
            <h1 className="text-5xl sm:text-6xl lg:text-7xl font-bold leading-tight text-slate-900 mb-6">
              I build modern React applications<br className="hidden sm:block" /> with clean, responsive UI.
            </h1>
            <p className="max-w-xl text-lg leading-8 text-slate-600 mb-8">
              I create responsive, mobile-friendly websites and web apps using React, Tailwind CSS, and modern design patterns.
            </p>
            <div className="flex flex-col items-center justify-center gap-4 sm:flex-row sm:justify-start">
              <a href="#work" className="inline-flex items-center gap-2 rounded-full bg-teal-700 px-8 py-3 text-sm font-semibold text-white shadow-lg shadow-teal-700/20 transition hover:bg-teal-600">
                View My Work
                <FaArrowRight />
              </a>
              <a href="#contact" className="inline-flex items-center gap-2 rounded-full border border-slate-300 bg-white px-8 py-3 text-sm font-semibold text-slate-700 transition hover:border-teal-700 hover:text-teal-700">
                Contact Me
                <FaArrowRight />
              </a>
            </div>
            <div className="mt-10 flex flex-wrap justify-center gap-3 text-sm text-slate-500 sm:justify-start">
              <span className="rounded-full border border-slate-200 bg-white px-4 py-2">React</span>
              <span className="rounded-full border border-slate-200 bg-white px-4 py-2">Tailwind CSS</span>
              <span className="rounded-full border border-slate-200 bg-white px-4 py-2">Responsive</span>
              <span className="rounded-full border border-slate-200 bg-white px-4 py-2">Vite</span>
            </div>
          </div>

          <div className="flex justify-center lg:justify-end">
            <div className="relative w-72 h-72 sm:w-80 sm:h-80 rounded-[2rem] overflow-hidden border-4 border-slate-300/40 bg-slate-100 shadow-2xl shadow-slate-200 transition duration-500 hover:-translate-y-2 hover:scale-[1.02]">
              <img className="w-full h-full object-cover transition-transform duration-700 hover:scale-110" src={assets.profileImg} alt="profile" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
''',
    'src/components/Skill.jsx': '''import { skillsData } from "../assets.js";

const Skill = () => {
  return (
    <section id="skills" className="py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-14">
          <p className="text-sm uppercase tracking-[0.4em] text-teal-700 font-semibold mb-4">My skills</p>
          <h2 className="text-4xl sm:text-5xl font-bold mb-4">
            <span className="text-teal-600">Technical</span> Skills
          </h2>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            These are the main tools and technologies I use while building interfaces and websites.
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {skillsData.map((skill) => (
            <div key={skill.title} className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">
              <h3 className="text-xl font-semibold text-slate-900 mb-4">{skill.title}</h3>
              <ul className="space-y-3 text-slate-600">
                {skill.items.map((item) => (
                  <li key={item} className="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3">
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Skill;
''',
    'src/components/Work.jsx': '''import Portfolio1 from "../assets/Portfolio1.jpg";
import Portfolio2 from "../assets/Portfolio2.jpg";
import Portfolio3 from "../assets/Portfolio3.jpg";
import Portfolio4 from "../assets/Portfolio4.jpg";

const images = [
  { src: Portfolio1, alt: "Portfolio project 1", title: "React Landing Page", description: "A responsive landing page built with React and Tailwind CSS." },
  { src: Portfolio2, alt: "Portfolio project 2", title: "Dashboard UI", description: "A clean dashboard interface designed for productivity and analytics." },
  { src: Portfolio3, alt: "Portfolio project 3", title: "Portfolio Clone", description: "A modern portfolio website demonstrating layout and design skills." },
  { src: Portfolio4, alt: "Portfolio project 4", title: "Agency Website", description: "A polished marketing website with interactive sections and graphics." },
];

const Work = () => {
  return (
    <section id="work" className="py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="mb-16 text-center">
          <p className="text-sm uppercase tracking-[0.4em] text-teal-700 font-semibold mb-4">Featured work</p>
          <h2 className="text-4xl font-bold text-slate-900 mb-4">Projects I&rsquo;ve Built</h2>
          <p className="text-lg text-slate-600 max-w-3xl mx-auto">
            Web applications built with modern layout techniques, strong usability, and responsive design.
          </p>
        </div>

        <div className="grid gap-7 md:grid-cols-2 xl:grid-cols-4">
          {images.map((image, index) => (
            <div key={index} className="group overflow-hidden rounded-[2rem] border border-slate-200 bg-white shadow-sm transition hover:-translate-y-1 hover:shadow-xl">
              <div className="overflow-hidden">
                <img src={image.src} alt={image.alt} className="h-56 w-full object-cover transition duration-500 group-hover:scale-105" />
              </div>
              <div className="p-6">
                <h3 className="text-lg font-semibold text-slate-900 mb-2">{image.title}</h3>
                <p className="text-sm leading-6 text-slate-600">{image.description}</p>
                <div className="mt-6 flex flex-wrap gap-3">
                  <a href="#" className="inline-flex rounded-full bg-teal-600 px-4 py-2 text-sm font-semibold text-white transition hover:bg-teal-500">Live Demo</a>
                  <a href="#" className="inline-flex rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-semibold text-slate-700 transition hover:border-teal-500 hover:text-teal-500">Source</a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Work;
''',
    'src/assets.js': '''import profileImg from './assets/profile.jpg';

export const assets = {
  profileImg,
};

export const navMenu = ['Home', 'About', 'Skills', 'Projects', 'Contact'];

export const skillsData = [
  {
    title: 'Frontend',
    items: ['React', 'JavaScript', 'HTML', 'CSS', 'Tailwind CSS'],
  },
  {
    title: 'Tools',
    items: ['Git', 'GitHub', 'VS Code', 'Vite'],
  },
  {
    title: 'UI & Layout',
    items: ['Responsive Design', 'Flexbox', 'Grid', 'Component Design'],
  },
];
''',
    'src/components/About.jsx': '''const About = () => {
  return (
    <section id="about" className="py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid gap-12 lg:grid-cols-[1.4fr_1fr] items-center">
          <div>
            <p className="mb-4 text-sm uppercase tracking-[0.4em] text-teal-700 font-semibold">About Me</p>
            <h2 className="text-4xl sm:text-5xl font-bold text-slate-900 mb-6">Building clean, responsive web experiences with React.</h2>
            <p className="text-lg leading-8 text-slate-600 mb-6">
              I’m a beginner frontend developer focused on creating modern websites using React, Tailwind CSS, and best design principles. I enjoy turning ideas into beautiful, responsive interfaces that feel smooth on every screen.
            </p>
            <ul className="grid gap-3 text-slate-700">
              <li className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">Responsive design for mobile, tablet, and desktop.</li>
              <li className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">Clean component structure using React and Tailwind CSS.</li>
              <li className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">Fast builds with Vite and a focus on usability.</li>
            </ul>
          </div>
          <div className="rounded-[2rem] border border-slate-200 bg-gradient-to-br from-white to-slate-100 p-8 shadow-xl">
            <h3 className="text-2xl font-semibold text-slate-900 mb-5">Quick facts</h3>
            <div className="space-y-4 text-slate-700">
              <div>
                <p className="text-sm text-slate-500">Location</p>
                <p>Pakistan</p>
              </div>
              <div>
                <p className="text-sm text-slate-500">Focus</p>
                <p>Frontend Web Applications</p>
              </div>
              <div>
                <p className="text-sm text-slate-500">Tools</p>
                <p>React, Tailwind CSS, Git</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
''',
    'src/components/Contact.jsx': '''import { FaEnvelope, FaGithub, FaLinkedin } from 'react-icons/fa';

const Contact = () => {
  return (
    <section id="contact" className="py-24 bg-slate-950 text-white">
      <div className="max-w-7xl mx-auto px-6">
        <div className="rounded-[2rem] border border-white/10 bg-white/5 p-10 shadow-2xl shadow-slate-950/20">
          <div className="max-w-3xl space-y-6">
            <p className="text-sm uppercase tracking-[0.4em] text-teal-400 font-semibold">Contact</p>
            <h2 className="text-4xl font-bold">Let’s build your next website together.</h2>
            <p className="text-slate-300 leading-8">
              If you have a project or want to connect, feel free to send a message. I’m available for freelance work and junior developer roles.
            </p>
            <a href="mailto:hello@example.com" className="inline-flex items-center gap-3 rounded-full bg-teal-500 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-teal-500/20 transition hover:bg-teal-400">
              <FaEnvelope /> Email me
            </a>
            <div className="flex flex-wrap gap-4 text-slate-200">
              <a href="https://github.com/" target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 rounded-full border border-slate-700 bg-white/5 px-4 py-3 transition hover:border-teal-400 hover:text-teal-300">
                <FaGithub /> GitHub
              </a>
              <a href="https://linkedin.com/" target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 rounded-full border border-slate-700 bg-white/5 px-4 py-3 transition hover:border-teal-400 hover:text-teal-300">
                <FaLinkedin /> LinkedIn
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;
'''
}

for path, content in files.items():
    Path(path).write_text(content, encoding='utf-8')
print('updated files')
