import { FaEnvelope, FaGithub, FaLinkedin } from 'react-icons/fa';

const Contact = () => {
  return (
    <section id="contact" className="py-24 bg-slate-950 text-white">
      <div className="max-w-7xl mx-auto px-6">
        <div className="rounded-2xl border border-white/10 bg-white/5 p-10 shadow-2xl shadow-slate-950/20">
          <div className="max-w-3xl space-y-6">
            <p className="text-sm uppercase tracking-widest text-teal-400 font-semibold">Contact</p>
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