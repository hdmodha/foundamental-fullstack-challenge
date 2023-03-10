import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  // fetch("localhost:20002/companies", {
  //   method: "GET",
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  // })
  //   .then((res) => res.json())S
  //   .then((data) => console.log(data));
  return (
    <div className={styles.container}>
      <h1>Hello</h1>
      <div></div>
    </div>
  );
};

export default Home;
