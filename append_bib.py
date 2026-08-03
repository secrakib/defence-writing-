import os

bibtex_entries = """
@inproceedings{bhattacharjee-etal-2023-banglanlg,
    title = "{B}angla{NLG} and {B}angla{T}5: Benchmarks and Resources for Evaluating Low-Resource Natural Language Generation in {B}angla",
    author = "Bhattacharjee, Abhik and Hasan, Tahmid and Ahmad, Wasi Uddin and Shahriyar, Rifat",
    booktitle = "Findings of the Association for Computational Linguistics: EACL 2023",
    year = "2023",
    pages = "726--735"
}

@article{nllb2022,
  title={No Language Left Behind: Scaling Human-Centered Machine Translation},
  author={NLLB Team and Costa-juss{\\`a}, Marta R. and others},
  journal={arXiv preprint arXiv:2207.04672},
  year={2022}
}

@article{tang2020multilingual,
  title={Multilingual translation with extensible multilingual pretraining and finetuning},
  author={Tang, Yuqing and Tran, Chau and Li, Xian and Chen, Peng-Jen and Goyal, Naman and Chaudhary, Vishrav and Gu, Jiatao and Fan, Angela},
  journal={arXiv preprint arXiv:2008.00490},
  year={2020}
}

@inproceedings{hu2021lora,
  title={LoRA: Low-Rank Adaptation of Large Language Models},
  author={Hu, Edward J and Shen, Yelong and Wallis, Phil and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
  booktitle={International Conference on Learning Representations},
  year={2022}
}

@inproceedings{papineni2002bleu,
  title={Bleu: a method for automatic evaluation of machine translation},
  author={Papineni, Kishore and Roukos, Salim and Ward, Todd and Zhu, Wei-Jing},
  booktitle={Proceedings of the 40th annual meeting of the Association for Computational Linguistics},
  pages={311--318},
  year={2002}
}

@inproceedings{popovic2015chrf,
  title={chrF: character n-gram F-score for automatic MT evaluation},
  author={Popovi{\\'c}, Maja},
  booktitle={Proceedings of the Tenth Workshop on Statistical Machine Translation},
  pages={392--395},
  year={2015}
}

@inproceedings{banerjee2005meteor,
  title={METEOR: An automatic metric for MT evaluation with improved correlation with human judgments},
  author={Banerjee, Satanjeev and Lavie, Alon},
  booktitle={Proceedings of the acl workshop on intrinsic and extrinsic evaluation measures for machine translation and/or summarization},
  pages={65--72},
  year={2005}
}

@inproceedings{snover2006study,
  title={A study of translation edit rate with targeted human annotation},
  author={Snover, Matthew and Dorr, Bonnie and Schwartz, Richard and Micciulla, Linnea and Makhoul, John},
  booktitle={Proceedings of the 7th Conference of the Association for Machine Translation in the Americas: Technical Papers},
  pages={223--231},
  year={2006}
}

@article{raffel2020exploring,
  title={Exploring the limits of transfer learning with a unified text-to-text transformer},
  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J},
  journal={Journal of Machine Learning Research},
  volume={21},
  number={140},
  pages={1--67},
  year={2020}
}

@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, {\\L}ukasz and Polosukhin, Illia},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}

@article{lewis2020bart,
  title={BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},
  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:1910.13461},
  year={2019}
}

@inproceedings{sennrich2015neural,
  title={Neural Machine Translation of Rare Words with Subword Units},
  author={Sennrich, Rico and Haddow, Barry and Birch, Alexandra},
  booktitle={Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={1715--1725},
  year={2016}
}

@article{wu2016google,
  title={Google's neural machine translation system: Bridging the gap between human and machine translation},
  author={Wu, Yonghui and Schuster, Mike and Chen, Zhifeng and Le, Quoc V and Norouzi, Mohammad and Macherey, Wolfgang and Krikun, Maxim and Cao, Yuan and Gao, Qin and Macherey, Klaus and others},
  journal={arXiv preprint arXiv:1609.08144},
  year={2016}
}
"""

with open(r'e:\Writing Defence\biblography.bib', 'a', encoding='utf-8') as f:
    f.write("\n" + bibtex_entries)
