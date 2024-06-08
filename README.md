<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<!-- <a name="readme-top"></a> -->

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Leo-Lsc/AutoData.git">
    <img src="images\logo.webp" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AutoData</h3>

  <p align="center">
    An Automated Framework to Construct Datasets for Assessing Knowledge Editing or Multi-Hop Reasoning Capability of Language Models.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#pip-installation">Pip-Installation</a></li>
      </ul>
    </li>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The data stored in language models (LMs) quickly becomes obsolete, and retraining these models from the ground up is often not feasible. Recently, various methods (e.g. [SERAC](https://github.com/eric-mitchell/serac), [IKE](https://github.com/Zce1112zslx/IKE), [MEND](https://github.com/eric-mitchell/mend), [KE](https://github.com/Hunter-DDM/knowledge-neurons), [ROME](https://github.com/kmeng01/rome), [MEMIT](https://github.com/kmeng01/memit), [FT-L](https://github.com/kmeng01/rome)) have been developed to inject new knowledge. 

Current methods mostly perform well in editing single atom facts, but they encounter catastrophic failures when tested on the ripple effects caused by the edited knowledge. For example, if we edit the information to state that the current President of the USA is Trump, then the answer to "Who is married to Trump?" should also change accordingly. 
While many datasets for evaluating knowledge editing of LMs exist, they predominantly focus on facts from Wikidata, primarily relating to people and events.
 
In other words, the data in these datasets is homogeneous and lacks diversity.
Besides, This type of dataset construction pipeline often inevitably involves parts such as manual annotation and crowdsourcing, leading to significant time and economic costs. Therefore, I implemented a framework, AutoData, that can automatically construct datasets containing various types of data based on specific needs.



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

<!-- This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ``` -->


You should have at least one API key from a large language model, preferably from [OpenAI](https://openai.com/index/openai-api/). 

### Pip Installation

<!-- Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ``` -->

```sh
git clone https://github.com/Leo-Lsc/AutoData.git
conda create -n AutoData python=3.11.8
cd AutoData
pip install -r requirements.txt
   ```


<!-- Overview -->
## Overview
AutoData is a framework that uses the LangChain library and OpenAI's API to automatically construct customized datasets. AutoData consists of five modules: [SubjectGenerator](autodata\subject_generator.py), [QA_Generator](autodata\QA_generator.py), [TripleExtractor](autodata\triple_extractor.py), [Interrupter](autodata\interruputer.py) and [TwoHopQuestionGenerator](autodata\two_hop_question_generator.py).

<!-- USAGE EXAMPLES -->
<!-- ## Use AutoData

### SubjectGenerator 


<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. Any contributions you make are **greatly appreciated**. Don't forget to give the project a star! Thanks!

<!-- Contributors -->
## Contributors

<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Leo-Lsc">
        <img src="https://avatars.githubusercontent.com/u/124846947?v=4" width="50" height="50" style="border-radius: 50%; overflow: hidden;" alt="Leo-Lsc"/>
        <br />
        <sub><b>Leo-Lsc</b></sub>
      </a>
    </td>
  </tr>
</table>


