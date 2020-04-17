import React from "react";

const NavLinks = () => {
  const links = [
    { text: "Home", link: "/" },
    { text: "About", link: "/about" },
    { text: "Contact", link: "/contact" },
    { text: "Privacy policy", link: "/portfolio" },
  ];
  return (
    <React.Fragment>
      {links.map((link, i) => (
        <li key={i}>
          <a className="">{link.text}</a>
        </li>
      ))}
    </React.Fragment>
  );
};

export default NavLinks;
