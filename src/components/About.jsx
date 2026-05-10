const About = () => {
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