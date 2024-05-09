You are an AI assistant who specializes in analyzing and summarizing scientific research papers. When given the details of a research paper, you should generate a JSON object that includes the following fields:
{
"title": "[PAPER_TITLE]",
"authors": ["[AUTHOR_1]", "[AUTHOR_2]", ...],
"publication_year": [YEAR],
"journal": "[JOURNAL_NAME]",
"doi": "[DOI_NUMBER]",
"abstract": "[ABSTRACT_TEXT]",
"key_findings": ["[FINDING_1]", "[FINDING_2]", ...],
"methodology": "[METHODOLOGY_DESCRIPTION]",
"implications": ["[IMPLICATION_1]", "[IMPLICATION_2]", ...]
}
Please fill in the placeholders with the relevant information from the provided research paper details. If any information is missing, use "N/A" for that field. Respond with code only.
Please analyze the following research paper and generate a JSON summary:

Title: The Effect of Social Media on Adolescent Mental Health
Authors: Emily Johnson, Michael Lee, Sarah Davis
Publication Year: 2022
Journal: Journal of Adolescent Psychology
DOI: 10.1037/0000123-456

Abstract: This study investigated the impact of social media use on the mental health of adolescents aged 13-18. A survey was conducted with 500 participants to assess their social media habits and mental well-being. The results showed a significant correlation between excessive social media use and increased levels of anxiety, depression, and low self-esteem. The findings highlight the need for interventions to promote healthy social media habits among adolescents.

Methodology: The study employed a cross-sectional survey design. Participants were recruited through schools and youth organizations. The survey included questions on social media use, mental health symptoms, and demographic information. Data were analyzed using regression analysis.

Key Findings:
Adolescents who spent more than 3 hours per day on social media had significantly higher levels of anxiety and depression compared to those who spent less time.
Negative feedback and social comparison on social media were strongly associated with low self-esteem.
Girls were more likely than boys to experience negative mental health outcomes related to social media use.

Implications:
Parents and educators should monitor adolescents' social media use and provide guidance on healthy habits.
Social media platforms should implement features to promote positive interactions and limit exposure to harmful content.
Mental health professionals should assess social media use as a potential factor in adolescent mental health issues.
