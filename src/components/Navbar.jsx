import { navMenu } from '../assets.js';
const Navbar = () => {
  return ( 
    <div className="fixed w-full py-4 z-50 backdrop-blur-3xl">
        <div className="container mx-auto px-6 max-w-7xl flex items-center justify-between">
            {/* Logo */}
            <div className="text-2xl font-bold text-zinc-800">
                <span>THE-</span>
                <span className="text-teal-800 font-orbitron"> Muzammmil Farooq</span>
                 </div>
                 {/*Menu*/}
                 
                 <div className="flex items-center space-x-8 border border-gray-200 rounded-full px-10 py-4 bg-white">
                    {navMenu.map((item, index) => (
                        <a key={index} href={`#${item}`} className="text-zinc-800 hover:text-teal-700">{item}</a>
                    ))}
                 </div>
            </div>
    </div>
    );
};

export default Navbar;