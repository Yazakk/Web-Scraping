import scrapy
import json
import collections
from ..items import JobstreetItem
from scrapy.loader import ItemLoader
from urllib.parse import urlparse, parse_qs, urlencode


class JobAdsSpider(scrapy.Spider):
    name = 'job_ads'
    allowed_domains = ['www.jobstreet.com.my']
    pages = list(range(1, 357))
    def start_requests(self):
        for page in self.pages:
            query = {
                "query": "query getJobs($country: String, $locale: String, $keyword: String, $createdAt: String, $jobFunctions: [Int], $categories: [String], $locations: [Int], $careerLevels: [Int], $minSalary: Int, $maxSalary: Int, $salaryType: Int, $candidateSalary: Int, $candidateSalaryCurrency: String, $datePosted: Int, $jobTypes: [Int], $workTypes: [String], $industries: [Int], $page: Int, $pageSize: Int, $companyId: String, $userAgent: String, $accNums: Int, $subAccount: Int, $minEdu: Int, $maxEdu: Int, $edus: [Int], $minExp: Int, $maxExp: Int, $seo: String, $searchFields: String, $candidateId: ID, $isDesktop: Boolean, $isCompanySearch: Boolean, $sort: String, $sVi: String, $duplicates: String, $flight: String, $solVisitorId: String) {\n  jobs(country: $country, locale: $locale, keyword: $keyword, createdAt: $createdAt, jobFunctions: $jobFunctions, categories: $categories, locations: $locations, careerLevels: $careerLevels, minSalary: $minSalary, maxSalary: $maxSalary, salaryType: $salaryType, candidateSalary: $candidateSalary, candidateSalaryCurrency: $candidateSalaryCurrency, datePosted: $datePosted, jobTypes: $jobTypes, workTypes: $workTypes, industries: $industries, page: $page, pageSize: $pageSize, companyId: $companyId, userAgent: $userAgent, accNums: $accNums, subAccount: $subAccount, minEdu: $minEdu, edus: $edus, maxEdu: $maxEdu, minExp: $minExp, maxExp: $maxExp, seo: $seo, searchFields: $searchFields, candidateId: $candidateId, isDesktop: $isDesktop, isCompanySearch: $isCompanySearch, sort: $sort, sVi: $sVi, duplicates: $duplicates, flight: $flight, solVisitorId: $solVisitorId) {\n    ...LegacyCompat_SearchResult\n    relatedSearchKeywords {\n      keywords\n      type\n      totalJobs\n    }\n  }\n}\n\nfragment LegacyCompat_SearchResult on SearchResult {\n  total\n  totalJobs\n  aigdpRelatedSearch\n  solMetadata\n  suggestedEmployer {\n    name\n    totalJobs\n  }\n  queryParameters {\n    key\n    searchFields\n    pageSize\n  }\n  gdpSearchAlgoGroup\n  experiments {\n    flight\n  }\n  jobs {\n    id\n    sourceCountryCode\n    isStandout\n    companyMeta {\n      id\n      isPrivate\n      name\n      logoUrl\n      slug\n    }\n    qualificationName\n    careerLevelName\n    workExperienceName\n    employmentTermName\n    jobTitle\n    jobUrl\n    jobTitleSlug\n    description\n    employmentTypes {\n      code\n      name\n    }\n    sellingPoints\n    locations {\n      code\n      name\n      slug\n      children {\n        code\n        name\n        slug\n      }\n    }\n    categories {\n      code\n      name\n      children {\n        code\n        name\n      }\n    }\n    postingDuration\n    postedAt\n    salaryRange {\n      currency\n      max\n      min\n      period\n      term\n    }\n    salaryVisible\n    bannerUrl\n    isClassified\n    solMetadata\n  }\n}\n",
                "variables": {
                    "keyword": "",
                    "jobFunctions": [

                    ],
                    "locations": [
                        50000
                    ],
                    "salaryType": 1,
                    "jobTypes": [

                    ],
                    "createdAt": "14d",
                    "careerLevels": [

                    ],
                    "page": page,
                    "country": "my",
                    "sVi": "[CS]v1|2FC9F35C0515DEA1-60000A35A196F193[CE]",
                    "solVisitorId": "59ce98e0-643f-4712-b437-6a72cbb3c52d",
                    "categories": [

                    ],
                    "workTypes": [

                    ],
                    "userAgent": "Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/86.0.4240.111%20Safari/537.36",
                    "industries": [

                    ],
                    "locale": "en"
                }
            }
            yield scrapy.Request(
                url='https://xapi.supercharge-srp.co/job-search/graphql?country=my&isSmartSearch=true',
                method='POST',
                body=json.dumps(query),
                headers={
                    'Content-Type': 'application/json'
                },
                callback=self.parse
            )

    def parse(self, response):
        # print(response.body)
        json_resp = json.loads(response.body)
        jobs = json_resp.get('data').get('jobs').get('jobs')
        for job in jobs:
            loader = ItemLoader(item=JobstreetItem())
            loader.add_value('ID', job.get('id'))
            loader.add_value('Date', job.get('postedAt'))
            loader.add_value('Location', job.get('locations')[0].get('name'))
            loader.add_value('Career_Level', job.get('careerLevelName'))
            loader.add_value('Work_Experience', job.get('workExperienceName'))
            loader.add_value('Job_Specialization_1', job.get('categories')[0].get('name'))
            loader.add_value('Job_Specialization_2', job.get('categories')[1].get('name'))
            loader.add_value('Employment_Type', job.get('employmentTermName'))
            loader.add_value('Company_Name', job.get('companyMeta').get('name'))
            loader.add_value('Qualifications', job.get('qualificationName'))
            # try:
            if job.get('salaryRange').get('min') is None:
                loader.add_value('Salary_Min', ['ND'])
            else:
                loader.add_value('Salary_Min', job.get('salaryRange').get('min'))

            if job.get('salaryRange').get('max') is None:
                loader.add_value('Salary_Max', ['ND'])
            else:
                loader.add_value('Salary_Max', job.get('salaryRange').get('max'))
            # except:
            #     loader.add_value('Salary_Min', ['ND'])
            #     loader.add_value('Salary_Max', ['Nd'])

            yield loader.load_item()












