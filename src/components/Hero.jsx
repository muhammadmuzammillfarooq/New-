import { FaArrowRight } from "react-icons/fa";
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
              I create responsive and user-friendly web applications using React, Tailwind CSS, and best design practices.
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
              <span className="rounded-full border border-slate-200 bg-white px-4 py-2">Vite</span>
              <span className="rounded-full border border-slate-200 bg-white px-4 py-2">Responsive UI</span>
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