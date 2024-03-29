START = r"""% LaTeX Cookbook, Packt Publishing, 2015
% Stefan Kottwitz
\documentclass[11pt,a4paper]{report}% compile with LuaLaTeX
%\usepackage[french]{babel}
\usepackage[utf8]{inputenc}
%\usepackage{lua-visual-debug}
\usepackage{sansmath}
\usepackage{mathtools}
\usepackage{graphicx} % utiliser des images seulement ou des figures seulement
\usepackage{lmodern}
\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{geometry}
\usepackage{listings} % utiliser les listes
\usepackage{graphicx} % utiliser des images seulement ou des figures seulement
\usepackage{xcolor} % for setting colors
\usepackage{color}
\usepackage{verbatim} % Package pour de grand morceaux de code brut
\usepackage{moreverb} % Permet de g\'erer les tabulations // \begin{verbatim}[4]
\usepackage{color}
\usepackage{float} % To place floating image
\usepackage{booktabs}
\usepackage{datatool}
\usepackage{csvsimple}
\usepackage{csquotes}
%\usepackage{dsfont}
%\usepackage{slashbox,multirow}
\usepackage{bookman}
\usepackage{textcomp}
\usepackage{eurosym}
\usepackage{numprint}
\definecolor{mygray}{rgb}{0.9,0.9,0.9}
\usepackage{appendix}
\usepackage[pdftex,colorlinks=true,linkcolor=black,citecolor=blue,urlcolor=blue]{hyperref}

\graphicspath{{../OutputFiles/}} %Setting the graphicspath

% set the default code style
\lstset{
    language=Python,
    frame=tb, % draw a frame at the top and bottom of the code block
    tabsize=4, % tab space width
    showstringspaces=false, % don't mark spaces in strings
    numbers=left, % display line numbers on the left
    commentstyle=\color{green}, % comment color
    keywordstyle=\color{blue}, % keyword color
    stringstyle=\color{red}, % string color
    backgroundcolor=\color{mygray}, % couleur de fond
    tabsize=4,
}

\title{!! NE PAS DIFFUSER !!
\\Rapport Financier}
\author{ROMAIN BOYRIE}
\date{DATE} 

\begin{document}

\pagestyle{headings}
%\frontmatter
\maketitle
%\mainmatter
\pagenumbering{arabic}
\setcounter{secnumdepth}{-1}
\tableofcontents
"""
CHAPITRE = r"""\chapter{TITRE}
"""
END = r"""
        
        \end{document}"""
CORPSSECTION = r"""

\section{TITRE}


\paragraph{Voici un présentation graphique du titre} : """

CORPSSITE = r"""(Ctrl + Clic)$<-$\href{SITE}{site web}"""
CORPSWIKI = r""", \href{WIKI}{wikipédia}"""
CORPSBOURSORAMA = r""", \href{BOURSORAMA}{boursorama}"""
CORPSLAPOSTE = r""", \href{LAPOSTE}{informations financières}"""
CORPSLEREVENU = r""", \href{LEREVENU}{informations journalistiques}"""
CORPS = r"""
\begin{figure}[!htb]
   \begin{minipage}{0.5\textwidth}
     \centering
     \includegraphics[width=.8\linewidth]{stockprice_close_TITRE.png}
     \caption{Cours et Volumes}\label{Fig:stockprice_close_TITRE}
   \end{minipage}\hfill
   \begin{minipage}{0.5\textwidth}
     \centering
     \includegraphics[width=.8\linewidth]{volatility_30_close_TITRE.png}
     \caption{Volatilité à 30 jours}\label{Fig:volatility_30_close_TITRE}
   \end{minipage}
\end{figure}
\begin{figure}[!htb]
   \begin{minipage}{0.5\textwidth}
     \centering
     \includegraphics[width=.8\linewidth]{mva_close_TITRE.png}
     \caption{Moyennes mobiles}\label{Fig:mva_close_TITRE}
   \end{minipage}\hfill
   \begin{minipage}{0.5\textwidth}
     \centering
     \includegraphics[width=.8\linewidth]{monaco_close_TITRE.png}
     \caption{Simulation Monte-Carlo}\label{Fig:monaco_close_TITRE}
   \end{minipage}
\end{figure}
\begin{figure}[!htb]
   \begin{minipage}{0.5\textwidth}
     \centering
     \includegraphics[width=.8\linewidth]{quantile_close_TITRE.png}
     \caption{Quantile}\label{Fig:quantile_close_TITRE}
   \end{minipage}\hfill
   \begin{minipage}{0.5\textwidth}
     \centering
     \includegraphics[width=.8\linewidth]{volatility_15_close_TITRE.png}
     \caption{Volatilité à 15 jours}\label{Fig:volatility_15_close_TITRE}
   \end{minipage}
\end{figure}
\begin{figure}[!htb]
   \begin{minipage}{0.5\textwidth}
     \centering
     \includegraphics[width=.8\linewidth]{prophet_close_TITRE.png}
     \caption{Prédictions}\label{Fig:prophet_TITRE}
   \end{minipage}\hfill
   \begin{minipage}{0.5\textwidth}
     \centering
     \includegraphics[width=.8\linewidth]{prophet_components_close_TITRE.png}
     \caption{Composantes Time Series}\label{Fig:prophet_components_TITRE}
   \end{minipage}
\end{figure}
\newpage
%\begin{figure}[!htb]
%   \begin{minipage}{0.5\textwidth}
%     \centering
%     \includegraphics[width=.8\linewidth]{volatility_7_close_TITRE.png}
%     \caption{Volatilité à 7 jours}\label{Fig:volatility_7_close_TITRE}
%   \end{minipage}\hfill
%   \begin{minipage}{0.5\textwidth}
%     \centering
%     \includegraphics[width=.8\linewidth]{volatility_3_close_TITRE.png}
%     \caption{Volatilité à 3 jours}\label{Fig:volatility_3_close_TITRE}
%   \end{minipage}
%\end{figure}
%\newpage
%\begin{figure}[!htb]
%   \begin{minipage}{0.5\textwidth}
%     \centering
%     \includegraphics[width=.8\linewidth]{volat_volub_30_close_TITRE.png}
%     \caption{Volume volatilité à 30 jours}\label{Fig:volat_volub_30_close_TITRE}
%   \end{minipage}\hfill
%   \begin{minipage}{0.5\textwidth}
%     \centering
%     \includegraphics[width=.8\linewidth]{volat_volub_15_close_TITRE.png}
%     \caption{Volume volatilité à 15 jours}\label{Fig:volat_volub_15_close_TITRE}
%   \end{minipage}
%\end{figure}
%\begin{figure}[!htb]
%   \begin{minipage}{0.5\textwidth}
%     \centering
%     \includegraphics[width=.8\linewidth]{volat_volub_7_close_TITRE.png}
%     \caption{Volume volatilité à 7 jours}\label{Fig:volat_volub_7_close_TITRE}
%   \end{minipage}\hfill
%   \begin{minipage}{0.5\textwidth}
%     \centering
%     \includegraphics[width=.8\linewidth]{volat_volub_3_close_TITRE.png}
%     \caption{Volume volatilité à 3 jours}\label{Fig:volat_volub_3_close_TITRE}
%   \end{minipage}
%\end{figure}
"""

TABLE = r"""
% Table generated by Excel2LaTeX from sheet 'Feuil1'
\begin{table}[H]
  \centering
    \begin{tabular}{|c|c|c|c|c|c|c|}
    \hline
    Prix & Séance & Risque  & Moy/ans & 5ans & 3ans & 1ans \\
    \hline
    PRIX &    ROR \%    & RISQUE & LOG \% & CINQ \% & TROIS \% & UN \% \\
    \hline
    \end{tabular}%
        \label{tab:table_TITRE}%
      \caption{Tableau de valeurs}
\end{table}%

"""

DESCRIPTION = r"""\paragraph{Ses activités sont : } ACTIVITE 

    """
